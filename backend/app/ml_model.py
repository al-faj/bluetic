import joblib, os
MODEL_PATH = os.getenv("MODEL_PATH", "./models/rf_model.pkl")

def predict_risk(features: dict):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not trained. Run train.py")
    model = joblib.load(MODEL_PATH)
    X = [[features.get("attendance",0), features.get("past_marks",0), features.get("activities_score",0)]]
    prob = model.predict_proba(X)[0,1]
    return {"risk_probability": float(prob)}
