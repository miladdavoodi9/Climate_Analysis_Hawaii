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
    return f"Welcome to the Climate APP!</br>"
    return f"Below are the available routes that can be taken...</br>"
    return f"/api/v1.0/precipitation</br>"
    return f"/api/v1.0/stations</br>"
    return f"/api/v1.0/tobs</br>"
    return f"/api/v1.0/[start_date format:yyyy-mm-dd]</br>"
    return f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]</br>"
    

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc())
    return jsonify(results)

    session.close()
    
    
    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    station = session.query(Measurement.station) 
    return jsonify(station)

    session.close()
    

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    #Query for the dates and temperatuyre obsercations from a year from the last data point
    date = session.query(Measurement.date).order_by(Measurement.date.desc())[0]
    last_date = dt.datetime.strptime(date[0], '%Y-%m-%d')
    year_before = last_date - relativedelta(years=1)
    filters = (Measurement.date >= year_before)

    temp = session.query(Measurement.date, Measurement.tobs).filter(filters).order_by(Measurement.date)
    
    return jsonify(temp)

    session.close()


@app.route("/api/v1.0/<start>" and "/api/v1.0/<start>/<end>")


    
# 4. Define main bahavior
if __name__ == "__main__":
    app.run(debug=True)
