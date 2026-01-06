import json
import logging
from app.queue import inference_queue
from app.ml.inference import SimpleAnomlyModel
from app.database import conn, cursor

logging.basicConfig(level=logging.INFO)

model = SimpleAnomlyModel(threshold=0.7)

def start_worker():
    while True:
        payload = inference_queue.get()

        try:
            if payload is None:
                continue

            # payload is a DICT
            prediction = model.predict(payload["values"])

            cursor.execute(
                "INSERT INTO sensor_data (device_id, timestamp, sensor_values, prediction, score) VALUES (?, ?, ?, ?, ?)",
                (
                    payload["device_id"],
                    payload["timestamp"],
                    json.dumps(payload["values"]),
                    prediction["prediction"],
                    prediction["score"]
                )
            )
            conn.commit()

            logging.info(f"Processed payload from {payload['device_id']}")

        except Exception as e:
            logging.error(f"Failed to process payload: {e}")

        finally:
            inference_queue.task_done()
