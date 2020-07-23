# Seattle_spins_analysis

TOC

Study of bike trips in Seattle 2015 - 2019
What kind of patterns are recognizable in the bike rider count data that Seattle collects hourly at 9 different locations throughout the city? Which of these patterns reach statistical significance?

Limitations--the bike count--while daily--is by no means a comprehensive count of bike trips. It is just a count of rides at the 9 different trip count locations. Nor do these counts tell us anything about why people choose to ride or why others choose not to. 

Data cleaning
- Datasets of hourly bike trip counts were obtained from the 10 active Seattle bike trip counter locations. While these datasets were reasonably complete and well-structured, there were several challenges to compiling them into one master datatable for useful analysis.
- During EDA, it was discovered that one of these sites did not come online until 2019. This site was not included in any of the analysis. 
- During EDA, it was discovered that data from several of the counter locations during 2014 was unreliable. Counts were 2-3x expectations. All data from this year was dropped.
- The preparation of raw dataset into a usable datatable required numerous steps. The first step was to read raw files from the city of Seattle's data portals in batches and append sets from the same site into one complete set. 
- Once a location's set was complete and contained hourly bike trip counts from 1/1/2014-6/30/2020, the next steps were to create day of week, month, and year columns from the date field and then aggregate each dataset by day while summerizing trip counts by am peak (5-9 am: assumed to be commuter trips) and other trips (an estimate of non-commuter trips: total trips - (commuter trip counts x 2)).
- A column with the count of bike shops within approx 2 miles of the bike trip counter location were added for each of the 9 bike trip counter locations.
- Each of the 9 bike trip counter location files were then merged by date into one master. Daily weather for Seattle (sourced by NOAA) info was added.
- Additional columns were then created on this master datatable.
-- Created total am peak trips and other trips, am peak trips for counter locations with 3 or less bike shops nearby and other trips for counter locations with more than 3
- During EDA, it was discovered that data from the NE Seattle counter location was missing for 3 months in the summer. Counts were much higher than expected in the month prior suggesting that this month's totals may have actually included some of the missing data, but clearly not all of it. Entries for these months were converted to NaN values so as to maintain the integrity of statistics and data visualization.

EDA
- Constructed visualizations of 
-- ave daily counts by AM Peak vs. Other
-- ave daily counts by day of week and peak vs non
-
-
