import json
from fastapi import FastAPI
from app.schemas import SensorPayload
from app.ml.inference import SimpleAnomlyModel
from app.queue import inference_queue
import threading
from app.worker import start_worker


model=SimpleAnomlyModel(0.7)

app = FastAPI(title="Edge AI Inference Backend")


@app.get("/metrics")
def metrics():
    return {
        "queue_size": inference_queue.qsize()
    }


@app.on_event("startup")
def start_background_worker():
    thread = threading.Thread(target=start_worker, daemon=True)
    thread.start()


@app.post("/ingest")
def ingest_data(payload: SensorPayload):

    inference_queue.put(payload.dict())

    return {
        "status":"queued"
    }
