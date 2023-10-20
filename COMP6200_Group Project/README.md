## Data Science Group Project (Group 100)
# Analysing Opal Users’ Transport Patterns in NSW and Exploring Predictive Demographic Variables

### Introduction:
In this project, we analyze the Opal usage data to show the patterns of use of bus, train, light rail, and ferry in different parts of NSW. Then, we link the demographic data from the census and closely analyze it to see if there is any relationships between transport patterns and demographic variables, such as income, age, households and population.

### Project Goals:
1. Describe patterns of different transportation modes using Opal usage
2. Identify some demographic variables that are significant to transport pattern
3. Establish predictive model for Opal usage

### Findings on Transport Patterns:
1. The maximum opal usage happened in late February with around 1.75 million usage, where the lowest usage was in mid-April with less than 100000 usage. *(the sharp fall in opal usage from April onwards is due to travel ban imposed by the government under COVID-19 restriction.)*
2. Weekdays generated more tap volume than weekends.
3. Midnight hours from 12am - 6am reported with fairly low usage. 8am and 5pm are the peak hours, which can be reasonably explained by the offices working hours in general.
4. Sydney CBD is the top region where people commonly travel to and from, followed by Paramatta, then North Sydney.
5. Train is the most popular transport in NSW, followed by bus. The opal usage for train is more than double of that for bus. Ferry is the least common transport in NSW.
6. The usage of train and bus seems to be largely affected by rush hours, while ferry seems to be least affected by that.

### Analysing Travel Patterns with Demographic Variables:
1. **K- means Clustering:** We start with clustering the data on travel pattern combined with demographics features, to understand the big picture of the features of opal users, and ideally identify some demographic feature which may affect the opal volume.
2. **Regression Analysis:** We use recursive feature elimination (RFE) to select features for our estimation model. 14 variables are manually selected to fit the model.
3. **Estimation Model (Multiple Linear Regression):** From the model, R-square is reported as 0.625, meaning 62.5% of tap volume can be explained by the independent variables, this is a moderately well model in explaining the volume of opal taps.

### Conclusion:
1. Train is the most popular transport in all times.
2. Tap-volume and transport patterns are more likely based on necessity to travel.
3. Regional income may have impact over the Tap-volume. This may due to purposes of travelling, implying most opal users may use public transports for work-purpose.



