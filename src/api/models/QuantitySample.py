from datetime import datetime
from src.api.models.QuantityTypes import QuantityTypes


class QuantitySample:
    # def __init__(self, id: str, quantity_type: QuantityTypes, quantity: float, start_date: datetime, 
    # end_date: datetime, workout_id: str) -> None:
    #     self.id = id
    #     self.quantity_type = quantity_type
    #     self.quantity = quantity
    #     self.start_date = start_date
    #     self.end_date = end_date
    #     self.workout_id = workout_id
    id: str
    quantity_type: QuantityTypes
    quantity: float
    start_date: datetime
    end_date: datetime
    workout_id: str