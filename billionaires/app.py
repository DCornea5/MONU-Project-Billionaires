# import necessary libraries
import os
from unicodedata import name
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from sympy import source
from sqlalchemy.orm import Session
from sqlalchemy import  Column, Integer, String, Float, JSON

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "postgresql://postgres:postgres@localhost:5432/billionaires"
# or "sqlite:///db.sqlite"


# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.drop_all()
db.create_all()

from .models import Billionaires


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index_leaflet.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["Name"]
        country = request.form["Country"]
                    
        networth = request.form["NetWorth"]
        age = request.form["Age"]
        source = request.form["Source"]
        rank = request.form["Rank"]
        
        lat = request.form["latitude"]
        lon = request.form["longitude"]
      

        billionaires = billionaires(name=name, country=country, networth=networth, age= age, source =source, rank = rank, lat=lat, lon=lon)
        db.session.add(billionaires)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")


@app.route("/api/billionaires")
def pals():
    results = db.session.query(Billionaires.name, Billionaires.country, Billionaires.networth, Billionaires.age, Billionaires.source, Billionaires.rank, Billionaires.lat, Billionaires.lon,).all()

    hover_text = [result[0] for result in results]
    name = [result[1] for result in results]
    country = [result[2] for result in results]
    networth = [result[3] for result in results]
    age = [result[4] for result in results]
    source = [result[5] for result in results] 
    rank = [result[6] for result in results]
    lat = [result[7] for result in results]
    lon = [result[8] for result in results]

    billionaires_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "lat": lat,
        "lon": lon,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(billionaires_data)


if __name__ == "__main__":
    app.run()
