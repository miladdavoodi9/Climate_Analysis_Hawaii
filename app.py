# 1. import Flask
from flask import Flask, jsonify
import numpy as np 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from dateutil.relativedelta import relativedelta
import datetime as dt 

#set up Database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect and exisiting database into a new model
Base = automap_base()
#reflect the tables
Base.prepare(engine,reflect=True)

#Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station 

# 2. create an app, being sure to pass name
app = Flask(__name__)

# 3. Define route
@app.route("/")
def welcome():
    return(
        f"Welcome to the Climate AP!</br>"
        f"Below are the available routes that can be taken...</br>"
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]</br>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]</br>"
    )
    

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc())

    session.close()
    
    all_precip = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precip.append(precipitation_dict)
    
    return jsonify(all_precip)
    
    
    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    station = session.query(Measurement.station) 

    session.close()
    
    all_stations = list(np.ravel(station))
    
    return jsonify(all_stations)
    

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    #Query for the dates and temperatuyre obsercations from a year from the last data point
    date = session.query(Measurement.date).order_by(Measurement.date.desc())[0]
    last_date = dt.datetime.strptime(date[0], '%Y-%m-%d')
    year_before = last_date - relativedelta(years=1)
    filters = (Measurement.date >= year_before)

    temp = session.query(Measurement.date, Measurement.tobs).filter(filters).order_by(Measurement.date)

    session.close()

    all_tobs = []
    for date, tobs in temp:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        all_tobs.append(temp_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start_date>")
def data_start(start_date):
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    total_list = []
    for min, avg, max in results:
        dict = {}
        dict["min_temp"] = min
        dict["avg_temp"] = avg
        dict["max_temp"] = max
        total_list.append(dict)

    session.close()
    return jsonify(total_list)

@app.route("/api/v1.0/<start_date>/<end_date>")
def all_dates(start_date, end_date):
    session = Session(engine)

    results = session.query(func.avg(Measurement.tobs), func.max(Measurement.tobs), func.min(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    series = []
    for avg, max, min in results:
        series_dict = {}
        series_dict["avg"] = avg
        series_dict["max"] = max
        series_dict["min"] = min
        series.append(series_dict)

    return jsonify(series)



    
# 4. Define main bahavior
if __name__ == "__main__":
    app.run(debug=True)
