from pydantic import BaseModel
from typing import List

class Sensor_payload(BaseModel):
    device_id:str
    timestamp:str
    values:List[float]
