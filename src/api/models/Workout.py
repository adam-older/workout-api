from typing import List

from src.api.models.Location import Location
from src.api.models.QuantitySample import QuantitySample

class Workout:
    # def __init__(self, id: str, total_distance: float, average_heart_rate: float, 
    # heart_rate_list: List[QuantitySample], locations_list: List[Location]) -> None:
        # self.id = id
        # self.total_distance = total_distance
        # self.average_heart_rate = average_heart_rate
        # self.heart_rate_list = heart_rate_list
        # self.locations_list = locations_list

    id: str
    total_distance: float
    average_heart_rate: float 
    heart_rate_list: List[QuantitySample]
    locations_list: List[Location]