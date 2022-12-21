# Surfs Up Analysis

## Overview
The purpose of this analysis was to use the dataset we were given to determine if a surf ‘n’ shake shop would be a sustainable business venture year-round in Oahu, Hawaii.  This was done by examining the dataset with sqlalchemy to see what temperatures are commonplace in the months of June and December.  After presenting our results for the temperature data, we state two additional sqlalchemy queries that we performed to gain additional insight into whether the surf 'n' shake shop is a practical business idea year-round.

## Results
In our analysis, we created two tables of temperature data for both June and December.  The following bulleted list showcases the significant findings of our analysis (with all temperatures stated being in Fahrenheit):

* For the month of June, we found that the mean temperature in Oahu was approximately 74.94 degrees, with a minimum temperature of 64 and a maximum temperature of 85 degrees.  The standard deviation is approximately 3.26 degrees, which suggests that the temperatures do not fluctuate significantly during the month of June.  While the minimum temperature of 64 degrees is probably lower than many people would enjoy surfing in, it is to be noted that this minimum temperature is nearly 3.5 standard deviations below the mean, meaning it is very unlikely that this minimum temperature would ever actually occur.    A screenshot of the table that contains the June temperature data is attached below. 
          
  <img width="150" alt="June_Temp_Summary_Statistics" src="https://user-images.githubusercontent.com/115128743/209015747-e8f40bab-f9d8-4306-a7d7-afb9c4a0b86e.png">


* For the month of December, we found that the mean temperature in Oahu was approximately 71.04 degrees, with a minimum temperature of 56 degrees and a maximum temperature of 83 degrees.  The standard deviation is approximately 3.75 degrees, suggesting that temperatures are slightly more unpredictable than in June, but that the temperatures in December also do not widely fluctuate.  In addition to this, we see that the minimum temperature is notably lower than the minimum temperature recorded in June.  Considering that the minimum temperature is over 4 standard deviations below the mean, it is very unlikely that this minimum temperature would be reached.  However, if temperatures did approach this minimum, it would be unlikely people would be interested in visiting the surf ‘n’ shake shop.  A screenshot of the table that contains the December temperature data is attached below. 

  <img width="170" alt="December_Temp_Summary_Statistics" src="https://user-images.githubusercontent.com/115128743/209016102-f23d8d75-0ada-4c6d-bbff-c55c0e6429c7.png">

* Judging from the consistent temperatures and small standard deviation, we can see that keeping the surf ‘n’ shake shop open during the month of June would likely be advisable. However, the surf ‘n’ shake shop owners may look into changing their business hours (or possibly closing for a brief period of time if the temperatures drop too significantly) during the month of December.  Though the colder temperatures in December could create problems, it seems likely that the surf ‘n’ shake shop should be able to stay open for the majority of the year, possibly making an exception for unusually cold days.

## Summary
As stated above, the surf ‘n’ shake shop should be able to maintain a fairly steady flow of business for the majority of the year, withstanding the occasional unusually cold temperatures.  If the shop does not want to significantly change its hours or close during times of colder weather, the owners may look into providing services/products that would still entice business.  These conclusions we have reached, though, have been based solely on the summary statistics of the temperature data we were provided.  To be more thorough in our analysis, we include two additional queries about the precipitation data from the different weather stations in Oahu.  

The goal of our first query was to determine which month out of June and December was rainier overall.  We see that in the following tables pictured below that June has more rainy days than December, though the data seems to suggest that when it does rain in December, it, on average, rains for longer/more intensely than it would on a rainy day in June.  This observation supports our previous conclusion that the surf 'n' shake shop may have to change their business hours during December if the temperatures are too low or if it rains heavily.

<img width="173" alt="June_Precipitation_Summary_Statistics" src="https://user-images.githubusercontent.com/115128743/209016400-5eeaf178-2683-4537-9a70-edc8730cda64.png"> <img width="194" alt="December_Precipitation_Summary_Statistics" src="https://user-images.githubusercontent.com/115128743/209016416-b38b2a8f-a02c-45cd-b099-06275404f377.png">


Also, we calculated the summary statistics of the precipitation data for each of the weather stations in Oahu, and we see that certain locations may not be the best to build a shake ‘n’ surf shop in.  For example, according to the two tables pictured below, stations USC00516128, USC00519281, and USC00513117 have the highest average precipitation per station than any other stations listed in the table for both the months of June and December.  In addition to this, these stations also have large numbers of recorded days in which precipitation occurred, suggesting that the areas in which these stations are located seem to consistently have higher amounts of precipitation.  So, in deciding where to build the surf 'n' shake shop, it may not be advisable to build the surf ‘n’ shake shop in locations near the three weather stations mentioned above.  The following screenshots show the summary statistics for each station in June and December, respectively. 
<img width="475" alt="June_Precipitation_Per_Station_DataFrame" src="https://user-images.githubusercontent.com/115128743/209016688-d3a60e74-ff73-4e36-85f0-5c268a2cfe42.png">   <img width="475" alt="December_Precipitation_Per_Station_DataFrame" src="https://user-images.githubusercontent.com/115128743/209016698-279cb34d-0684-483d-bce7-141ee4aca7ed.png">



