from datetime import datetime

class Location:
    # def __init__(self, id: str, latitude: float, longitude: float, altitude: float,
    # horizontal_accuracy: float, vertical_accuracy: float, timestamp: dt.datetime, speed: float,
    # speed_accuracy: float, course: float, course_accuracy: float) -> None:
    #     self.id = id
    #     self.latitude = latitude
    #     self.longitude = longitude
    #     self.altitude = altitude
    #     self.horizontal_accuracy = horizontal_accuracy
    #     self.vertical_accuracy = vertical_accuracy
    #     self.timestamp = timestamp
    #     self.speed = speed
    #     self.speed_accuracy = speed_accuracy
    #     self.course = course
    #     self.course_accuracy = course_accuracy

    id: str
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