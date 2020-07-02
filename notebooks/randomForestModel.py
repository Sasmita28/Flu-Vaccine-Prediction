import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
from sklearn.preprocessing import OneHotEncoder, scale, StandardScaler, MinMaxScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, average_precision_score,classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, Bidirectional, LSTM, Reshape,TimeDistributed, GRU, concatenate, add,Input
import pickle
import tensorflow as tf
from sklearn.model_selection import cross_val_score

# import data
df_training = pd.read_csv("training_set_features.csv")
df_labels = pd.read_csv("training_set_labels.csv")
df = df_labels.merge(df_training, on = "respondent_id", how = "inner")

# Clean feature and label dataset
df1 = df.drop(["health_insurance","employment_industry", "employment_occupation"], axis=1)
df2 = df1.dropna()
df_y = df2.select_dtypes(include=['int64'])
df_y = df_y["h1n1_vaccine"]
df_y = np.array(df_y)

# Preprocess labels
df_y = df2.select_dtypes(include=['int64'])
df_y = df_y["h1n1_vaccine"]
df_y = np.array(df_y)

# Preprocess features
df_x = df2.drop(["respondent_id","h1n1_vaccine", "seasonal_vaccine"], axis=1)
df_categories = df_x.select_dtypes(include=['object'])
df_float = df_x.select_dtypes(include=['float64'])
features_array = np.array(df_categories)
float_array = np.array(df_float)
encoder = OneHotEncoder(sparse=False)
onehot = encoder.fit_transform(features_array)
df_features = np.concatenate((float_array, onehot),axis=1)
min_max_scaler = MinMaxScaler()
df_features = min_max_scaler.fit_transform(df_features)

# Separate features and labels into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df_features, df_y, random_state=42)

#Define Model Instances
model_optimal = RandomForestClassifier(n_estimators = 100, random_state=42)

#Fit Model
model_optimal.fit(X_train,y_train)

#Save Model
filename = 'randomForestML.sav'
joblib.dump(model_optimal, filename)