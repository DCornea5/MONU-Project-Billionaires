import pandas as pd
import plotly.express as px
import numpy as np
import geopandas as gpd
from bs4 import BeautifulSoup
import requests
import pymongo
from pymongo import MongoClient
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import psycopg2

import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Float
# %load_ext sql
# %sql sqlite://

from config import user, password
user = user
password = password
import json
import config
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func