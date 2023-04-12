from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

class LocationModel(SQLModel, table = True):
    location_id: Optional[int] = Field(default = None, primary_key = True)
    guid: str
    workout_id: int
    latitude: float
    longitude: float
    altitude: float
    horizontal_accuracy: float
    vertical_accuracy: float
    timestamp: datetime
    speed: float
    speed_accuracy: float
    course: float
    course_accuracy: float