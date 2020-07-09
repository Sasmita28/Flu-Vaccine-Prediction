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

# from config1 import password
app = Flask(__name__)

# DATABASE_URL will contain the database connection string:
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://uasjdajzsygssk:5ca12565ad331228d31a1594bcb08d0fc05df5838a583df924b9c1b66aa7bcc2@ec2-18-214-119-135.compute-1.amazonaws.com:5432/d3tagolmi6l9pb"

db = SQLAlchemy(app)
# engine = create_engine()


# Create connection
# conn = engine.connect()
# Begin transaction




@app.route("/")
def index():
    return render_template("index.html")
    # return "flu vaccine machine learning project"



# @app.route("/query")
# def query():
    
#     # engine = create_engine('postgresql://postgres:sasmita@localhost/vaccine_db')
#     # conn = engine.connect()
#     trans = conn.begin()
#     data = conn.execute('SELECT * FROM '
#                         '"flu_vaccine_prediction"')
#     json_data = jsonify(data)
#     return json_data

#     trans.commit()
#     # Close connection
#     conn.close()


if __name__ == "__main__":
    app.run(debug=True)
