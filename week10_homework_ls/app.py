from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd
import datetime as dt

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return(
        f"Welcome to the Hawaii climate analysis API!<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"<br/>"
        f"<br/>"
        f"<br/>"
        f"*For /api/v1.0/start and  /api/v1.0/start/end please replace word START and END with<br/>"
        f" dates format YYYY-MM-DD<br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    #################################################
    # Create SQL object
    #################################################
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # reflect an existing database into a new model
    Base = automap_base()
    # reflect the tables
    Base.prepare(engine, reflect=True)

    # Save references to each table
    Measurement = Base.classes.measurement
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #get date on year before the latest date in the datasete
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Selection precipitation and date
    sel = [func.avg(Measurement.prcp), Measurement.date]
    #query filtering and ordering by date
    precipitation = session.query(*sel).\
                order_by(func.strftime(Measurement.date).asc()).\
                filter(Measurement.date >= query_date).\
                group_by(Measurement.date).all()
    #convert query results into a Data Fame
    query_df = pd.DataFrame(precipitation, columns=["prcp","date"])
    #Changing index to date
    #query_df["date"] = pd.to_datetime(query_df["date"])
    query_df.set_index(query_df["date"], inplace=True)
    #keeping only prco and station columns
    query_df = query_df.loc[:,["prcp"]]

    return jsonify(list(query_df.to_dict().values()))

@app.route("/api/v1.0/stations")
def stations():
    #################################################
    # Create SQL object
    #################################################
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # reflect an existing database into a new model
    Base = automap_base()
    # reflect the tables
    Base.prepare(engine, reflect=True)

    # Save references to each table
    
    Station = Base.classes.station

    # Create our session (link) from Python to the DB
    session = Session(engine)

    #query the base to get the distinct stations
    station = session.query(Station.station).distinct(Station.station).all()
    #convert query results into a Data Fame
    query_df = pd.DataFrame(station, columns=["station"])
    #Return JSON
    return jsonify(list(query_df.to_dict().values()))

@app.route("/api/v1.0/tobs")
def tobs():
    #################################################
    # Create SQL object
    #################################################
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # reflect an existing database into a new model
    Base = automap_base()
    # reflect the tables
    Base.prepare(engine, reflect=True)

    # Save references to each table
    Measurement = Base.classes.measurement
    

    # Create our session (link) from Python to the DB
    session = Session(engine)

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query for the tobs from one year onwards before the last date
    tobs = session.query(Measurement.date, Measurement.tobs).\
                        filter(Measurement.date >= query_date).\
                        order_by(func.strftime(Measurement.date).asc()).all()
    #Convert query results into a Data Frame
    query_df = pd.DataFrame(tobs, columns=["date","tobs"])
    #Change index for date
    query_df.set_index(query_df["date"], inplace=True)
    #keeping only prco and station columns
    query_df = query_df.loc[:,["tobs"]]

    return jsonify(list(query_df.to_dict().values()))

@app.route("/api/v1.0/<start>")
def average_start(start):
    #################################################
    # Create SQL object
    #################################################
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # reflect an existing database into a new model
    Base = automap_base()
    # reflect the tables
    Base.prepare(engine, reflect=True)

    # Save references to each table
    Measurement = Base.classes.measurement

    # Create our session (link) from Python to the DB
    session = Session(engine)

    temps = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                          filter(Measurement.date >= start).all() 
    #Convert query results into a Data Frame
    query_df = pd.DataFrame(temps, columns=["min","avg","max"]).transpose()

    return jsonify(list(query_df.to_dict().values()))

@app.route("/api/v1.0/<start>/<end>")
def average_period(start, end):
    #################################################
    # Create SQL object
    #################################################
    engine = create_engine("sqlite:///Resources/hawaii.sqlite")

    # reflect an existing database into a new model
    Base = automap_base()
    # reflect the tables
    Base.prepare(engine, reflect=True)

    # Save references to each table
    Measurement = Base.classes.measurement

    # Create our session (link) from Python to the DB
    session = Session(engine)

    temps = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                          filter(Measurement.date >= start).filter(Measurement.date <= end).all() 
    #Convert query results into a Data Frame
    query_df = pd.DataFrame(temps, columns=["min","avg","max"]).transpose()

    return jsonify(list(query_df.to_dict().values()))

if __name__ == "__main__":
    app.run(debug=True)