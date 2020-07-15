from flask import Flask, render_template, request, jsonify, json, redirect
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import json
import ast
import os
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String, Float
import select
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base

# from config1 import password

Base = declarative_base()

app = Flask(__name__)


# DATABASE_URL will contain the database connection string:


from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') 
engine = create_engine('postgres://smudpxfmokljmy:7f3da7db55ebfa4fd7e026f8e4ab6d98406914c9071522869954e1260363fc26@ec2-34-237-89-96.compute-1.amazonaws.com:5432/dcck9ut83mpkjl')
# Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# print('DATABASE_URL' : DATABASE_URL)

@app.route("/")
def index():
    return render_template("index.html")
    # return "flu vaccine machine learning project"



@app.route("/query")
def query():


    conn = engine.connect()
    data = pd.read_sql("SELECT * FROM flu_vaccine_prediction", conn)
    json_data = data.to_json(orient ='records')
    return json_data

if __name__ == "__main__":
    app.run(debug=True)
