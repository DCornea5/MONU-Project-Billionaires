# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models import Billionaires


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index_leaflet.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        Counts = request.form["Counts"]
        lat = request.form["latitude"]
        lon = request.form["longitude"]

        Billionaires = Billionaires(Country=Counts, lat=lat, lon=lon)
        db.session.add(Billionaires)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")


@app.route("/api/Billionaires")
def pals():
    results = db.session.query(Billionaires.counts, Billionaires.latitude, Billionaires.longitude).all()

    hover_text = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

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
