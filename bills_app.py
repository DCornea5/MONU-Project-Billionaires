
#################################################
# Import/ call dependencies and Setup
#################################################
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import MongoClient
import datetime as dt



#################################################
# Import file scrap_billsthat contains all scrapping functions
#################################################
import scrape_bills
from config import password

#################################################
# Create an instance of Flask, set static url path as coded in .html files
#################################################
app = Flask(__name__,
            static_url_path='', 
            static_folder='static/',
            template_folder='templates/')

CORS(app)



connect_string = 'mongodb+srv://bpr:PpeorELP1XJAow8j@cluster0.d6noj.mongodb.net/test'
# client = MongoClient(connect_string)
# db = client.get_default_database()


#################################################
# Use PyMongo to establish Mongo connection for database mars_app
#################################################
mongo = PyMongo(app, uri=connect_string)


#################################################
# Route to render index.html template using data from MongoDB
#################################################
@app.route("/")
@app.route("/index")
def home():

    # Find one lastest record of data from the mongo database
    mongo_data = mongo.db.forbes_data.find_one()

    print(f"\n\n---------------------------------->mongo DB rendering ....\n\n")
    # Return the hompage/index page with mars_data (alias mars)
    return render_template("index.html", bills=mongo_data)

#################################################


#################################################
# Route to another page
#################################################
@app.route("/leaflet")
def leaflet():
    return(render_template("index_leaflet.html"))

@app.route("/dimple")
def dimple():
    return(render_template("index_dimple.html"))

@app.route("/industries_view")
def ind_view():
    return(render_template("industries_view.html"))

@app.route("/about_us")
def aboutUs():
    return(render_template("about_us.html"))

@app.route("/billionaire_profile")
def profile():
    return(render_template("billionaires_profile.html"))

@app.route("/map_age")
def map_age():
    return(render_template("density_map_age.html"))

@app.route("/net_worth")
def map_networth():
    return(render_template("billionaires_netWorth.html"))

#################################################


#################################################
# Route to page /jsonData
#################################################
@app.route("/jsonData")
def jsonifyData():
    jsonData = scrape_bills.jsonifyData()
    return jsonify(jsonData)
#################################################


#################################################
# Route that triggers the scrape function
#################################################
@app.route("/scrape")
def scrape():

    # Execute all the scrape functions and get the returned data
    bills_data = scrape_bills.scrape()

    print(f"\n\n------------------>read data from scrape<------------------\n\n\n")

    # Load the data that just had been scrapped to the database
    mongo.db.forbes_data.update_one({}, {"$set": bills_data}, upsert=True)
   
    print(f"\n\n---------------------------------->mongo DB calling ....\n\n\n")

    # Return to the homepage
    return redirect("/")
#################################################


#################################################
if __name__ == "__main__":
    app.run(debug=True)
