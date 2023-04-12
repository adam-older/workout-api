from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

from .LocationModel import LocationModel
from .QuantitySampleModel import QuantitySampleModel

class WorkoutModel(SQLModel, table=True):
    workout_id: Optional[int] = Field(default = None, primary_key = True)
    guid: str
    total_distance: float
    average_heart_rate: float 
    # heart_rate_list: List[QuantitySampleModel]
    # locations_list: List[LocationModel]