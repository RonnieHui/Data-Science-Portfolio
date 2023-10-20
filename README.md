# Data-Science-Portfolio

This repository describes the portfolio tasks of course unit COMP6200 in S2 2021 at Macquarie University. 

## About Portfolio 1
The goal of portfolio 1 is to perform some exploration and analysis on data of cyclying activities that include GPS location data as well as some measurements related to cycling performace like heart rate and power.

#### About the Data:
The files _(Calga_RR_2016.gpx', 'Calga_TT_2016.gpx', 'Calga_RR_2019.gpx' and 'Calga_TT_2019.gpx')_ were exported from Strava and represent four cyclying races by Steve Cassidy in 2016 and 2019. Two are time trials where the rider rides alone on a set course. Two are road races where the rider rides with a peleton. All were held on the same course but the road races include two laps where the time trials include just one.

#### Data Exploration:
1. Summary of total distance for each ride
2. Summary of speeds for each ride
3. Compare the speeds in time trials between 2016 and 2019
4. Summary of average speeds in state of climbing, descending or flat
5. Summary of development for each ride as an indicator of gear usage

#### Key Findings:
1. Total distances in road races are around double of that in time trials for both 2016 and 2019, which is in line with the fact that road races include two laps.
2. Road races are faster than time trials in both 2016 and 2019 with an average speed of 1.48km/h faster in 2016 and 0.82km/h faster in 2019. The maximum speed in road race is 92.75km/h, which is 24.89km/h higher than time trial in 2016. Whereas, the maximum speed in road race is 70.37km/h, which is 7.07km/h higher than time trial in 2019.
3. The average speeds in the two time trials are 33.45km/h in 2016 and 33.06km/h in 2019 respectively. The speed is on average 0.39km/h faster in 2016.
4. The average speeds when descending is the highest, followed by flat, then climbing. 
5. The development patterns are similar in all rides, large proportion of low development indicates the rider was climbing hills at most of the time.



## About Portfolio 2
The goal of portfolio 2 is to explore data from the Federal Government Sport Vouchers program that provides up to two $100 vouchers for kids to participate in organised sport. Secondly, find out whether the voucher program is used equally by parents in low, middle and high socioeconomic areas by using the Socio-Economic Indexes for Areas (SEIFA) data from ABS.

#### About the Data:
The data _(sportsvouchersclaimed.csv)_ comes from the _data.gov.au_ website and provides details of all Sport Vouchers that have been redeemed since February in 2015 as part of the Sport Voucher program. The data is from South Australia.   

The data _(ABS_SEIFA_LGA.csv)_ comes from the Australian Bureau of Statistics which shows a few measures of Socioeconomic Advantage and Disadvantage for every Local Government Area.

#### Data Exploration:
1. Distribution of vouchers by LGA 
2. Distribution of vouchers by Sport
3. Distribution pattern of popular sports in different parts of South Australia
4. Voucher Usage by Electorates
5. Relationship between SEIFA measures and voucher usage

#### Key Findings:
1. Top 5 regions participated in the Sport Voucher program in South Australia are Onkaparinga, Salisbury, Tea Tree Gully, Charles Sturt and Playford.
2. Top 5 favorable sports in this Sport Voucher program are Australian Rules, Netball, Football, Gymnastics and Basketball.
3. Australian Rules and Netball are the most popular sports among most of the region in South Australia. Onkaparinga is the most active region participated in this sport voucher program, followed by Tea Tree Gully, Charles Sturt and Salisbury.
4.  Voucher clamied per person of top 10 electorates range from \\$7.27 to \\$23.60. Flinders has the highest voucher claimed per person (\\$23.60). On the other hand, Voucher clamied per person of least 10 electorates range from \\$0.3 to \\$0.97. Dunstan has the lowest voucher claimed per person (\\$0.30).
5. SEIFA measures have no or very little relation with voucher usage.

#### Conduct similar analysis to Queensland's Dataset:
1. Top 5 regions participated in teh Sport Voucher program in Queensland are Gold Coast, Brisbane, Logan, Sunshine Coast and Moreton Bay.
2. Toop 5 favorable sprots are Rugby League, Football (Soccer), Netball, Gymnastics and Australian Rules.
3. Rugby League and Football (Soccer) are the most popular sports among most of the region in Queensland. Gold Coast is the most active region in claiming sport voucher, followed by Brisbane, Logan and Sunshine Coast.
4.  The average voucher claimed in Queensland is $0.07 per person, which is much less than that of South Australia.
5. SEIFA measures have significant relation with voucher usage.



## About Portfolio 3
The goal of portfolio 3 is to build and evaluate a predictive model for customer churn rate of a telecommunications company from available features.

#### About the Data:
The data is provided in file _MobileCustomerChurn.csv_. It was generated by Hume Winzar at Macquarie based on a real dataset provided by Optus. The data consists of some numerical variables _(such as Account/Service/Plan tenure in months, Total number of services under an account, Age, Monthly access fee payable, etc)_ and some categorical variables _(such as State location of registered service, Used equipment brand, Whether the customer is on a BYO (bring your own) plan, contract status, etc)_.

#### Data Exploration:
1. Data cleaning was performed to remove NA values and some unrelated columns were filtered out for analysis purposes. 
2. **Perform basic analysis on churn and numerical variables:**
    * a. Churn rate is: 38.51%
    * b. Check correlations between churn and numerical variables
    * c. Compare the means in numerical variables for churn vs no churn
3. **Perform basic analysis on churn and categorical variables:**
    * a. Look into each categorical variable
    * b. Look at the distribution of churn by categorical variables

#### Building Prediction Model:
1. Create dummy variables for all categorical variables for running logistic regression
2. Use Recursive Feature Elimination (RFE) to select features for analysis
3. Run logistic regression using statistic model to select significant variables
4. Build the prediction model with final selected features:
    * Account tenure, age, month of contract remaining, last fixed contract duration, monthly spending, customer in Country region, service provided in Australian Capital Territory, Queensland and Western Australia

#### Evaluation of the Model: 
1. Do predictions on test set
2. Accuracy score is 0.71
3. Confusion matrix shows there are 5,274 correct predictions and 2,107 incorrect predictions
4. Receiver Operating Characteristic (ROC) curve indicates it is a good classifier
