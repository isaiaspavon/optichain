# 🚛 OptiChain – AI-Powered Supply Chain Route Planner

OptiChain is a full-stack logistics intelligence tool that uses **real-time weather**, **machine learning**, and a **modern UI** to estimate delivery ETAs based on live conditions.

Built with ❤️ using:
- 🧠 Python + FastAPI for ML ETA prediction
- ☕ Java + Spring Boot backend
- 🛰️ Open-Meteo API for weather forecasting
- 🖥️ Angular frontend for internal tooling

---

## 📸 Demo

![OptiChain Screenshot](link-to-screenshot-if-you-want.png)

---

## 📦 Features

| Feature | Description |
|--------|-------------|
| 🌦️ Live Weather Data | Pulls real-time weather using Open-Meteo |
| 🧠 ML ETA Prediction | Uses a regression model trained on synthetic delivery data |
| 🚚 Route Simulation | Calculates ETA from distance + weather |
| 🖥️ Angular UI | Modern internal dashboard with form input and results display |
| 🌐 Fullstack API Flow | Angular → Spring Boot → FastAPI → ML → Back again |

---

## 🚀 How to Run It

### 1. Start the ML Server (FastAPI)
```bash
cd ml-engine
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python predict_eta.py
uvicorn app:app --reload
```

### 2. Start the Java Backend (Spring Boot)

```bash
cd backend-java
./mvnw spring-boot:run
```

### 3. Start the Angular Frontend
```bash
cd frontend-angular
npm install
npm run start
```
## 🌐 Visit the App

📍 [http://localhost:4200](http://localhost:4200)

## 🌤️ Sample Output (Frontend)

After entering:

- **Latitude:** `33.7490`  
- **Longitude:** `-84.3880`  
- **Distance:** `300`

You’ll get a response like:

```json
{
  "eta_minutes": 10.5,
  "weather_used": {
    "temperature_c": 20.4,
    "wind_speed_kmh": 17.8,
    "weather_code": 0
  },
  "input": {
    "latitude": 33.749,
    "longitude": -84.388,
    "distance_km": 300,
    "temperature_c": 20.4,
    "wind_speed_kmh": 17.8,
    "weather_code": 0
  }
}
```

## 🧠 Tech Stack

| Layer         | Tech                     | Purpose                          |
|---------------|--------------------------|----------------------------------|
| Frontend      | Angular 17               | Form, API call, result display   |
| Backend       | Java 17 + Spring Boot    | Weather fetch, ML coordination   |
| ML Engine     | Python + FastAPI         | Predict ETA from inputs          |
| External API  | Open-Meteo               | Live weather data                |
| Bonus         | CORS Config + REST       | Clean and modular integration    |

---

## 💼 Resume-Ready Bullet Point

> Built a fullstack supply chain simulator using Java (Spring Boot), Angular, and Python (FastAPI). Integrated real-time weather APIs and ML-based ETA prediction to simulate delivery planning. Created modular components and RESTful services for an extensible internal logistics tool.

---

## 📌 Stretch Goals (Optional)

- 🗺️ Add Leaflet.js for map route visualization  
- 🧾 Route logging with MongoDB or PostgreSQL  
- 📤 Upload routes via CSV  
- 🔐 Firebase or Google OAuth for internal login  
- ⚙️ CI/CD with GitHub Actions or Railway Deploy

---

## 🧠 Inspiration

OptiChain was inspired by real-world logistics and internal tool engineering roles at companies like Google, FedEx, and UPS. These types of systems simulate backend infrastructure that powers supply chains, real-time ETA forecasts, and route planning decisions.

---

## 🧪 Fun Facts

- ML model is trained on synthetic data but can be retrained with real datasets  
- Weather code is simplified to: `0 = clear`, `1 = rain`, `2 = snow`  
- Entire app runs locally and offline (excluding external weather API)  
- Backend and ML communicate over REST — fully modularized microservice-style

---

## 📬 Contact

Made with ❤️ by [@isaiaspavon](https://github.com/isaiaspavon) 💪  
Let me know if you want to collab or deploy your own version — I'm here to help!
