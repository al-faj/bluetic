import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import joblib
import os

N = 1000
np.random.seed(42)
attendance = np.random.beta(5,2,N) * 100
past_marks = np.random.normal(60,15,N)
activities = np.random.uniform(0,10,N)
risk = ((attendance < 60) & (past_marks < 50)).astype(int)

df = pd.DataFrame({"attendance": attendance, "past_marks": past_marks, "activities_score": activities, "risk": risk})

X = df[["attendance","past_marks","activities_score"]]
y = df["risk"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
pred = model.predict_proba(X_test)[:,1]
print("AUC:", roc_auc_score(y_test, pred))

os.makedirs("../models", exist_ok=True)
joblib.dump(model, "../models/rf_model.pkl")
print("Model saved to ../models/rf_model.pkl")      
