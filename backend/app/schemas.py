from pydantic import BaseModel,Field
from typing import List

class SensorPayload(BaseModel):
    device_id:str=Field(...,min_length=1)
    timestamp:float
    values:List[float]=Field(...,min_items=1,max_items=20)
