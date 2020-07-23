# Seattle_spins_analysis

TOC

## Study of bike trips in Seattle 2015 - 2019
What kind of patterns are recognizable in the bike rider count data that Seattle collects hourly at 9 different locations throughout the city? Which of these patterns reach statistical significance?

### Background
In 2014, the city of Seattle expanded its bike trip counter program to gain a better understanding of bike trip patterns. Sub-surface and reflective counters were placed in 12 different locations along greenways and bike commuter corridors. (Three are no longer in service and one new one was added in 2019). The stated goal was to get a measure of baseline ridership that could guide investments in infrastructure to help the city reach its goal of increasing bike ridership by 400% by 2030. Since 2014, dedicated bike only bike lanes have been added in the city--most notably along 2nd Ave through the central district of the city. Some planned projects have been eliminated due to lack of community and government support. 

Seattle ranks somewhere in the middle of the top of the pack regarding bike friendliness and bike commuter ridership. According to the [2014 American Community Survey](http://bikeleague.org/sites/default/files/Where_We_Ride_2014_data_web.pdf#12) analysis of bike commuting in cities, 3.7% of people bike to work in Seattle which placed it 24th among cities with populations over 65,000.

### Limitations
The bike count--while daily--is by no means a comprehensive count of bike trips. It is just a count of rides at the 9 different trip count locations. Nor do these counts tell us anything about why people choose to ride or why others choose not to. Also, riders on a single trip could be counted at more than one location if their trip happened to pass by multiple counter locations. The likelihood of this happening increases with longer trips since more counters could be encountered, and with certain commuter trips since counters are located at the heads and tails of 

## Data cleaning
- Datasets of hourly bike trip counts were obtained from the 10 active Seattle bike trip counter locations. While these datasets were reasonably complete and well-structured, there were several challenges to compiling them into one master datatable for useful analysis.
- The preparation of raw dataset into a usable datatable required numerous steps. The first step was to read raw files from the city of Seattle's data portals in batches and append sets from the same site into one complete set. 
- Once a location's set was complete and contained hourly bike trip counts from 1/1/2014-6/30/2020, the next steps were to create day of week, month, and year columns from the date field and then aggregate each dataset into a daily count of trips during am peak (5-9 am: assumed to be commuter trips) and other trips (an estimate of non-commuter trips: total trips - (commuter trip counts x 2)). The reason for subtracting 2x am peak counts from the total count was to allow 'other trip counts' to be a proxy for recreational trip counts. 
- A column with the count of bike shops within approx 2 miles of the bike trip counter location was added for each of the 9 bike trip counter locations.
- Each of the 9 bike trip counter location files were then merged by date into one master. Daily weather for Seattle (sourced by NOAA) info was added.
- Additional columns were then created on this master datatable:
> - Created total am peak trips and other trips, 
> - Created summary columns of am peak trip counts (and other trip counts) for counter locations with 'fewer' bike shops nearby (3 or less) and 'many' bike shops nearby (4 or more)
## EDA
- During EDA, it was discovered that one of these sites did not come online until 2019. This site was not included in any of the analysis. 
- During EDA, it was discovered that data from several of the counter locations during 2014 was unreliable. Counts were 2-3x expectations. All data from this year was dropped.
- 2020 has been such an anomaly that it too was dropped from analysis. It may be interesting to perform analysis on data from this year at a future date.
- During EDA, it was discovered that data from the NE Seattle counter location was missing for 3 months in the summer. Counts were much higher than expected in the month prior suggesting that this month's totals may have actually included some of the missing data, but clearly not all of it. Entries for these four months were converted to NaN values so as to maintain the integrity of statistics and data visualization.
- Numerous preliminary visualizations were performed to better understand some of the patterns in the data. Some of the results were surprising.
> - Bike trip counts did not reveal an increase in overall bike trip counts from 2015-2019.
> - Bike trip counts during the am peak were lower than bike trip counts at other times of the day and lower than anticipated.
> - Bike trip counts exhibit a strong seasonal pattern--less so for am peak commuter trip counts and more so for counts from other times of day.
> - AM peak (weekday only) bike trip counts exhibit a pattern by day of week. Trip counts peak on Tuesday and Wednesday and are lowest on Friday.
> - Counts of bike trips at the Fremont bike trip counter location were 3-4 times higher than the next highest location. Some statistical analysis was performed without Fremont counts to prevent it from overshadowing the results.

## Visualizations and statistical analysis
-- ave daily counts by AM Peak vs. Other
-- ave daily counts by day of week and peak vs non
-
-
