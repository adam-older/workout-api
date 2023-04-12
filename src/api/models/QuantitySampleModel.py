from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

from .QuantityType import QuantityType


class QuantitySampleModel(SQLModel, table = True):
    sample_id: Optional[int] = Field(default = None, primary_key = True)
    guid: str
    workout_id: int
    quantity_type: QuantityType
    quantity: float
    start_date: datetime
    end_date: datetime
    workout_id: str