from flask import Flask, render_template, request, jsonify, json, redirect
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import json
import ast
import os
import pandas as pd

app = Flask(__name__)


# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"
engine = create_engine('postgresql://postgres:sasmita@localhost/vaccine_db')
# Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# vaccine_db = SQLAlchemy(app)



@app.route("/")
def index():
    return render_template("index.html")
    # return "flu vaccine machine learning project"



@app.route("/query")
def query():
    engine = create_engine('postgresql://postgres:sasmita@localhost/vaccine_db')
    conn = engine.connect()
    data = pd.read_sql("SELECT * FROM flu_vaccine_prediction", conn)
    json_data = data.to_json(orient ='records')
    return json_data


if __name__ == "__main__":
    app.run(debug=True)