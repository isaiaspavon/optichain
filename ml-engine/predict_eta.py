# This script generates fake logistics data
# (distance, temp, wind, condition) and trains
# a regression model. It then saves it as model.pkl

import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Generate synthetic dataset
np.random.seed(42)
n_samples = 500

data = {
    "distance_km": np.random.uniform(10, 1000, n_samples),
    "temperature_c": np.random.uniform(-10, 35, n_samples),
    "wind_speed_kmh": np.random.uniform(0, 50, n_samples),
    "weather_code": np.random.randint(0, 3, n_samples),  # 0 = Clear, 1 = Rain, 2 = Snow
}

df = pd.DataFrame(data)

# Simulated ETA in minutes (base = distance/avg speed)
df["eta_minutes"] = (
    df["distance_km"] / np.random.uniform(40, 70) +
    df["wind_speed_kmh"] * 0.3 +
    df["weather_code"] * 15 +  # snow/rain adds delay
    np.random.normal(0, 5, n_samples)  # noise
)

# Train model
features = ["distance_km", "temperature_c", "wind_speed_kmh", "weather_code"]
X = df[features]
y = df["eta_minutes"]

model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
