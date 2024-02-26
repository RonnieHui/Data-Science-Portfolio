import datetime
import os
from airflow import DAG
from airflow import models
from airflow.contrib.operators.bigquery_operator import BigQueryOperator 
from airflow.contrib.operators.bigquery_to_gcs import BigQueryToCloudStorageOperator
from airflow.operators.dummy_operator import DummyOperator

today_date = datetime.datetime.now().strftime("%Y%m%d")
table_name_p4 = 'propane-shell-363803.ecommerce.total_unique_visitors'
table_name_p5 = 'propane-shell-363803.ecommerce.total_unique_visitors_by_channel'
table_name_p12 = 'propane-shell-363803.ecommerce.avg_quantity_per_order'
yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time()) 

default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately when it is 
    # detected in the Cloud Storage bucket.
    'start_date': yesterday,
    # To email on failure or retry set 'email' arg to your email and enable emailing here.
    'email_on_failure': False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting at least 5 minutes 
    'retries': 0,
    'retry_delay': datetime.timedelta(minutes=5),
    'project_id': models.Variable.get('gcp_project')
}

with DAG(dag_id='daily_queries_dag',
    schedule_interval=datetime.timedelta(days=1), 
    default_args=default_dag_args) as dag:

    start = DummyOperator(task_id='start', dag = dag)

    bq_query_p4 = BigQueryOperator(
        task_id='bq_query_p4', 
        sql=f"""SELECT COUNT(*) AS product_views, 
        COUNT(DISTINCT fullVisitorId) AS unique_visitors 
        FROM `data-to-insights.ecommerce.all_sessions`;""", 
        destination_dataset_table=table_name_p4, 
        gcp_conn_id='bigquery_default', 
        use_legacy_sql=False, 
        write_disposition='WRITE_TRUNCATE', 
        create_disposition='CREATE_IF_NEEDED', 
        dag=dag)

    bq_query_p5 = BigQueryOperator(
        task_id='bq_query_p5', 
        sql= f"""SELECT channelGrouping AS referring_site,
        COUNT(DISTINCT fullVisitorId) AS unique_visitors
        FROM `data-to-insights.ecommerce.all_sessions`
        GROUP BY referring_site
        ORDER BY unique_visitors DESC;""", 
        destination_dataset_table=table_name_p5, 
        gcp_conn_id='bigquery_default', 
        use_legacy_sql=False, 
        write_disposition='WRITE_TRUNCATE', 
        create_disposition='CREATE_IF_NEEDED', 
        dag=dag)

    bq_query_p12 = BigQueryOperator(
        task_id='bq_query_p12', 
        sql = f"""WITH unique_order_by_person  AS (
            SELECT
            fullVisitorId,
            (v2ProductName) AS product_name,
            COUNT(productQuantity) AS orders,
            SUM(productQuantity) AS quantity
            FROM `data-to-insights.ecommerce.all_sessions`
            GROUP BY fullVisitorId, product_name)
            SELECT 
            product_name,
            COUNT(*) AS unique_view,
            SUM(orders) AS total_orders,
            SUM(quantity) AS total_quantity,
            (SUM(quantity)/SUM(orders)) AS avg_quantity_per_order
            FROM unique_order_by_person
            GROUP BY product_name
            ORDER BY unique_view DESC
            LIMIT 5;""", 
        destination_dataset_table=table_name_p12, 
        gcp_conn_id='bigquery_default', 
        use_legacy_sql=False, 
        write_disposition='WRITE_TRUNCATE', 
        create_disposition='CREATE_IF_NEEDED', 
        dag=dag)
        

    export_p12 = BigQueryToCloudStorageOperator(
        task_id = 'export_p12',
        source_project_dataset_table = 'propane-shell-363803:ecommerce.avg_quantity_per_order', 
        destination_cloud_storage_uris = 'gs://us-central1-ecommerce-a595d264-bucket/avg_quantity_per_order_result.csv',
        export_format='CSV', print_header=True)


    end = DummyOperator(task_id='end', dag = dag)

start >> bq_query_p4 >> bq_query_p5 >> bq_query_p12 >> export_p12 >> end
