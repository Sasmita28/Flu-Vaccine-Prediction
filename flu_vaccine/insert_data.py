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

app = Flask(__name__)
# load our prediction dataset to pandas

df = pd.read_csv('sample_prediction_set.csv')

# DATABASE_URL will contain the database connection string:

engine = create_engine("postgres://uasjdajzsygssk:5ca12565ad331228d31a1594bcb08d0fc05df5838a583df924b9c1b66aa7bcc2@ec2-18-214-119-135.compute-1.amazonaws.com:5432/d3tagolmi6l9pb")

# Create a metadata instance
metadata = MetaData(engine)
# Declare a table
table = Table('flu_vaccine_prediction',metadata,
Column('respondent_id',Integer),
Column('id',Integer, primary_key= True),                        
Column('h1n1_vaccine', Integer),                   
Column('seasonal_vaccine', Integer),
Column('h1n1_concern' ,  Float),               
Column('h1n1_knowledge' , Float),               
Column('behavioral_antiviral_meds', Float),     
Column('behavioral_avoidance', Float),           
Column('behavioral_face_mask' ,Float),         
Column('behavioral_wash_hands', Float),        
Column('behavioral_large_gatherings', Float),    
Column('behavioral_outside_home',  Float),      
Column('behavioral_touch_face', Float),         
Column('doctor_recc_h1n1',  Float),             
Column('doctor_recc_seasonal',Float),           
Column('chronic_med_condition',  Float),        
Column('child_under_6_months' ,Float),  
Column('health_worker',   Float),  
Column('opinion_h1n1_vacc_effective',Float),   
Column('opinion_h1n1_risk' ,  Float),  
Column('opinion_h1n1_sick_from_vacc',Float), 
Column('opinion_seas_vacc_effective' , Float),  
Column('opinion_seas_risk' ,  Float),     
Column('opinion_seas_sick_from_vacc',  Float), 
Column('age_group' ,  String),    
Column('education', String),  
Column('race' , String),  
Column('sex' ,  String),   
Column('income_poverty', String), 
Column('marital_status', String),  
Column('rent_or_own',  String),  
Column('employment_status' ,  String), 
Column('hhs_geo_region' ,String),  
Column('census_msa'  ,    String),   
Column('household_adults',   Float),   
Column('household_children',   Float),    
Column('Prediction' ,     Integer) )
# Create all tables
metadata.create_all()

df.to_sql(name='flu_vaccine_prediction',con=engine, if_exists='replace', index=False)

print('Data Uploaded!')




