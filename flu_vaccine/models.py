from .app import vaccine_db


class Flu_Vaccine(vaccine_db.Model):
    __tablename__ = 'flu_vaccine_prediction'

    id = vaccine_db.Column(vaccine_db.Integer, primary_key=True)
    respondent_id= vaccine_db.Column(vaccine_db.Integer)
    h1n1_vaccine = vaccine_db.Column(vaccine_db.Integer)
    seasonal_vaccine = vaccine_db.Column(vaccine_db.Integer)
    h1n1_concern = vaccine_db.Column(vaccine_db.Float)
    h1n1_knowledge = vaccine_db.Column(vaccine_db.Float)               
    behavioral_antiviral_meds =vaccine_db.Column(vaccine_db.Float)    
    behavioral_avoidance = vaccine_db.Column(vaccine_db.Float)         
    behavioral_face_mask  = vaccine_db.Column(vaccine_db.Float)      
    behavioral_wash_hands = vaccine_db.Column(vaccine_db.Float)      
    behavioral_large_gatherings = vaccine_db.Column(vaccine_db.Float) 
    behavioral_outside_home  = vaccine_db.Column(vaccine_db.Float)     
    behavioral_touch_face = vaccine_db.Column(vaccine_db.Float)          
    doctor_recc_h1n1  = vaccine_db.Column(vaccine_db.Float)              
    doctor_recc_seasonal = vaccine_db.Column(vaccine_db.Float)           
    chronic_med_condition  = vaccine_db.Column(vaccine_db.Float)      
    child_under_6_months = vaccine_db.Column(vaccine_db.Float) 
    health_worker   = vaccine_db.Column(vaccine_db.Float)  
    opinion_h1n1_vacc_effective = vaccine_db.Column(vaccine_db.Float)   
    opinion_h1n1_risk   = vaccine_db.Column(vaccine_db.Float)  
    opinion_h1n1_sick_from_vacc = vaccine_db.Column(vaccine_db.Float) 
    opinion_seas_vacc_effective  = vaccine_db.Column(vaccine_db.Float) 
    opinion_seas_risk   =vaccine_db.Column(vaccine_db.Float)      
    opinion_seas_sick_from_vacc  = vaccine_db.Column(vaccine_db.Float) 
    age_group =vaccine_db.Column(vaccine_db.VARCHAR(30))      
    education = vaccine_db.Column(vaccine_db.VARCHAR(30))
    race  = vaccine_db.Column(vaccine_db.VARCHAR(30))  
    sex  =  vaccine_db.Column(vaccine_db.VARCHAR(30))
    income_poverty = vaccine_db.Column(vaccine_db.VARCHAR(30))
    marital_status = vaccine_db.Column(vaccine_db.VARCHAR(30)) 
    rent_or_own =  vaccine_db.Column(vaccine_db.VARCHAR(30)) 
    employment_status   = vaccine_db.Column(vaccine_db.VARCHAR(30))
    hhs_geo_region =  vaccine_db.Column(vaccine_db.VARCHAR(30))  
    census_msa     = vaccine_db.Column(vaccine_db.VARCHAR(30))   
    household_adults  = vaccine_db.Column(vaccine_db.Float)   
    household_children  =  vaccine_db.Column(vaccine_db.Float)  
    Prediction     =  vaccine_db.Column(vaccine_db.Integer)
        

    def __repr__(self):
        return '<FLu_Vaccine %r>' % (self.id)
