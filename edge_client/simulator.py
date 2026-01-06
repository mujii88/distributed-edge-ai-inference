import time
import random
import requests

BACKEND_URL = "http://127.0.0.1:8000/ingest"

device_id='eddge-001'

while True:
    payload={
        'device_id':'device_id',
        'timestamp':time.time(),
        'values':[random.random() for i in range(5)]
    }

    r=requests.post(BACKEND_URL,json=payload)

    print(r.json())
    time.sleep(5)