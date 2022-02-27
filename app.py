# import dependencies
from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################

# Create an app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return render_template('index.html')


# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation'...")
    # Create session from Python to DB
    session = Session(engine)

    # Query all precipitation data
    precip = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()

    # Create a dictionary and convert to date as the key and prcp as the value
    precipRecordings = []
    for date, prcp in precip:
        precip_dict = {date: prcp}
        precipRecordings.append(precip_dict)

    # Return the JSON representation of the dictionary.
    return jsonify(precipRecordings)

# Station route
@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations'...")
    # Create session from Python to  DB
    session = Session(engine)

    # Return a JSON list of stations from the dataset.
    stations = session.execute('SELECT DISTINCT station from station').fetchall()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stations))

    return jsonify(all_stations)


# TOBs route
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'TOBs'...")
    # Create session from Python to DB
    session = Session(engine)

    # Return a list of dates and temperature observations of the most active station for the last year of data.
    activeStation = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-23').filter(Measurement.station == 'USC00519281').order_by(Measurement.date).all()

    session.close()

    # Return a JSON list of temperature observations (TOBS) for the last year of data.
    activeStationtemps = list(np.ravel(activeStation))
    return jsonify(activeStationtemps)


# Temp stats by start date
@app.route("/api/v1.0/<start>")
def startdate(start):
    print(f"Server received request for 'temps'... start: {start}")
    # Create session from Python to DB
    session = Session(engine)

    # Return a list of dates and temperature observations of the most active station for the last year of data.
    tempsByDate = session.query(func.max(Measurement.tobs).label('max_temp'), func.min(Measurement.tobs).label('min_temp'), func.avg(Measurement.tobs).label('avg_temp')).filter(Measurement.date >= start).order_by(Measurement.date).all()

    session.close()
    print(tempsByDate)
    # When given the start date, calculate min, max and average for all dates greater than or equal to the start date.
    tempRecordings = [{'date range': f'{start} to 2017-08-23'},
    {'max temp': tempsByDate[0][0]},
    {'min temp': tempsByDate[0][1]},
    {'avg temp': tempsByDate[0][2]}]
    tempStats = list(np.ravel(tempRecordings))

    # Return the JSON representation of the dictionary.
    return jsonify(tempStats)

# Temp stats between start/end dates
@app.route("/api/v1.0/<start>/<end>")
def betweendates(start, end):
    print(f"Server received request for 'temps'... start: {start} end: {end}")
    # Create session from Python to DB
    session = Session(engine)

    # Return a list of dates and temperature observations of the most active station for the last year of data.
    tempsByDate = session.query(func.max(Measurement.tobs).label('max_temp'), func.min(Measurement.tobs).label('min_temp'), func.avg(Measurement.tobs).label('avg_temp')).filter(Measurement.date >= start).filter(Measurement.date <= end).order_by(Measurement.date).all()

    session.close()
    print(tempsByDate)
    # When given the start date, calculate min, max and average for all dates greater than or equal to the start date.
    tempRecordings = [{'date range': f'{start} to {end}'},
    {'max temp': tempsByDate[0][0]},
    {'min temp': tempsByDate[0][1]},
    {'avg temp': tempsByDate[0][2]}]
    tempStats = list(np.ravel(tempRecordings))

    # Return the JSON representation of the dictionary.
    return jsonify(tempStats)


if __name__ == "__main__":
    app.run(debug=True)