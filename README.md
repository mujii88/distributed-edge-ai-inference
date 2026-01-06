🧠 Distributed Edge AI Inference System

A production-style edge-to-cloud AI inference pipeline where edge devices send sensor data to a backend that performs asynchronous ML inference and stores results.

This project demonstrates backend engineering, system design, and applied ML inference.

🚀 Features

Edge device sensor data simulation

FastAPI backend for data ingestion

Asynchronous inference queue

Background worker for ML inference

SQLite persistence (sensor data + predictions)

Modular and scalable architecture

🏗️ Architecture
Edge Device → FastAPI API → Inference Queue → Worker → ML Inference → Database

🧠 Tech Stack

Python

FastAPI

Pydantic

SQLite

Queue-based async processing

Logging

📂 Structure
backend/
 ├── app/
 │   ├── main.py
 │   ├── database.py
 │   ├── schemas.py
 │   ├── queue.py
 │   └── ml/inference.py
 └── worker.py
edge_client/
 └── simulator.py

⚙️ Run
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
python backend/worker.py
python edge_client/simulator.py

📊 Sample Response
{
  "status": "stored",
  "prediction": {
    "prediction": "Normal",
    "score": 0.67
  }
}

🎯 Key Learnings

Asynchronous backend design

Edge-to-cloud AI workflows

ML inference in production systems

Queue-based scalability patterns

👤 Author

Mujtaba Ahmed
Final-year Electrical Engineering student | Edge AI & Distributed Systems