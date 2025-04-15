# FastAPI serving hosting /predict-eta POST endpoint 
# that takes route + weather info and returns the ETA

# Test the ML model by running:
#   source venv/bin/activate
#   python predict_eta.py
#   uvicorn app:app --reload
#   {
#       "distance_km": 250,
#       "temperature_c": 22,
#       "wind_speed_kmh": 5,
#       "weather_code": 1
#   }
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class RouteInput(BaseModel):
    distance_km: float
    temperature_c: float
    wind_speed_kmh: float
    weather_code: int  # 0=Clear, 1=Rain, 2=Snow

@app.post("/predict-eta")
def predict_eta(data: RouteInput):
    features = np.array([[data.distance_km, data.temperature_c, data.wind_speed_kmh, data.weather_code]])
    eta = model.predict(features)[0]
    return {"eta_minutes": round(eta, 2)}
