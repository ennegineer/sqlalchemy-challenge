# SQLAlchemy - Surfs Up!

We're off to Honolulu, Hawaii! To help with trip planning, we need to do some climate analysis on the area. The following outlines what we'll do.

## Step 1 - Climate Analysis and Exploration
Using Python and SQLAlchemy, we've done basic climate analysis and data exploration of the climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


### Precipitation Analysis
* First we found the most recent date in the data set.
* Using this date, we retrieved the last 12 months of precipitation data by querying the 12 preceding months of data.
* The results are plotted using the DataFrame `plot` method.

### Station Analysis
* We queried to calculate the total number of stations in the dataset.
* We then designed a query to find the most active stations.
  * List the stations and observation counts in descending order.
  * Using the most active station ID, calculated the lowest, highest, and average temperature.
* Next we designed a query to retrieve the last 12 months of temperature observation data (TOBs).
  * Filter by the station with the highest number of observations.
  * Query the last 12 months of temperature observation data for this station.
  * Display the results as a histogram.

- - -

## Step 2 - Climate App
Open app.py to view Flask APIs based on the queries developed in the analysis.

### Routes
* `/`
  * index.html loads from Flask template reader.
  * This home page lists all routes that are available.

- - -

## Other Analyses
* The following analyses are in the [temp_analysis_bonus_1_starter.ipynb] and [temp_analysis_bonus_2_starter.ipynb] starter notebooks.

### Temperature Analysis I
* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Using pandas to perform the following:
  * Convert the date column format from string to datetime.
  * Identify the average temperature in June at all stations across all available years in the dataset. 
  * Do the same for December temperature.

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. We used an unpaired t-test because we are comparing exactly two populations of data.

### Temperature Analysis II
* Looking to take a trip from August first to August seventh of this year, we will use historical data in the dataset find out what the temperature has previously looked like.
* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.
* Using the `calc_temps` function we calculate the min, avg, and max temperatures for the trip dates, using the matching dates from a previous year (i.e., using "2017-08-01").
* The bar chart shows the min, avg, and max temperature from the previous query.


### Daily Rainfall Average
* Calculate the rainfall per weather station using the previous year's matching dates.
  * Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.

### Daily Temperature Normals
* Calculate the daily normals for the duration of your trip. Normals are the averages for the min, avg, and max temperatures. You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.

  * Set the start and end date of the trip.
  * Use the date to create a range of dates.
  * Strip off the year and save a list of strings in the format `%m-%d`.
  * Use the `daily_normals` function to calculate the normals for each date string and append the results to a list called `normals`.
  * Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
  * Use Pandas to plot an area plot for the daily normals.

- - -
