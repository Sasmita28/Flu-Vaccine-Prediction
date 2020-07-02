-- Create a new table

CREATE TABLE Flu_Vaccine_prediction (
respondent_id INT NOT NULL,
id   INT NOT NULL PRIMARY KEY,                        
h1n1_vaccine INT NOT NULL,                   
seasonal_vaccine INT NOT NULL,
h1n1_concern   FLOAT,               
h1n1_knowledge  FLOAT,               
behavioral_antiviral_meds FLOAT,     
behavioral_avoidance FLOAT,           
behavioral_face_mask  FLOAT,         
behavioral_wash_hands FLOAT,        
behavioral_large_gatherings FLOAT,    
behavioral_outside_home  FLOAT,      
behavioral_touch_face FLOAT,         
doctor_recc_h1n1  FLOAT,             
doctor_recc_seasonal FLOAT,           
chronic_med_condition  FLOAT,        
child_under_6_months FLOAT,  
health_worker   FLOAT,  
opinion_h1n1_vacc_effective FLOAT,   
opinion_h1n1_risk   FLOAT,  
opinion_h1n1_sick_from_vacc FLOAT, 
opinion_seas_vacc_effective  FLOAT,  
opinion_seas_risk   FLOAT,     
opinion_seas_sick_from_vacc  FLOAT, 
age_group   vARCHAR(30),    
education VARCHAR(30),  
race       vARCHAR(30),  
sex   vARCHAR(30),   
income_poverty vARCHAR(30), 
marital_status vARCHAR(30),  
rent_or_own  vARCHAR(30),  
employment_status   vARCHAR(30), 
hhs_geo_region  vARCHAR(30),  
census_msa      vARCHAR(30),   
household_adults   FLOAT,   
household_children   FLOAT,    
Prediction      INT ) ;             