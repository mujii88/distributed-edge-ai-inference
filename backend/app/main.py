from fastapi import FastAPI
from app.schemas import Sensor_payload

app=FastAPI(title='Edge AI Inference Backend')

@app.post('/ingest')
def ingest_data(payload:Sensor_payload):
    return {
        'status':'received',
        'device_id':payload.device_id,
        'num_features':len(payload.values)
    }