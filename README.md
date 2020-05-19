# Climate Analysis Hawaii

## Climate Analysis and Exploration
Use Python, SQLAlchemy, ORM queries, Pandas, and Matplotlib to do basic climate analysis and data exploration of the climate database.
  - Use SQLAlchemy to explore different tables in dataset
  - Dataset includes two tables; Measurement and Stations
      - Measurement: station, date, precipitation, and time of observation
      - Station: station, name, lat, lng, and elevation
  
Precipitation Analysis
  - Design a query to retrieve the last 12 months of precipitation data
  - Load results into dataframe, set index to date, and plot

Plot Precipitation differences by date
![](graphs/Precipation%20by%20Date.png)
  
Station Analysis
  - Design a query to calculate the total number of stations
  - Design a query to find the most active stations
     - List the stations and observation counts in descending order
     - Which station has the highest number of observations? Lowest? Average? etc..
  - Design a query to retrieve the last 12 months of termperature observation data (tobs)
     - Filter by stations with the highest number of observations
     - Plot the results as histogram
     - ![](graphs/Histogram_Temperature%20Frequency.png)
  
## Climate API
  - Design a Flask API based on queries that have been deployed and return JSON called data
  
  Routes
  - /
    - Home page
    - List all routes that are available
  - /api/v1.0/precipitation
  - /api/v1.0/stations
  - /api/v1.0/tobs
  - /api/v1.0/<start> and /api/v1.0/<start>/<end>
    - Given the start only date, calculate minimum, maximum, and average for all dates greater than
    - Given the start and end dates, calculate the minimum, maximum and average for dates inclusive of range given
  
