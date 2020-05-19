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
     ![](graphs/Histogram_Temperature%20Frequency.png
  
Climate API
  - Create routes to include data found and return JSON data through Flask API
