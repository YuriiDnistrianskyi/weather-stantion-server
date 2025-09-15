from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from typing import Dict, Any
from datetime import datetime
from project import db
from project.ORM.domain.i_dto import IDTO
from project.ORM.domain.orders.weather_station import WeatherStation

class Info(db.Model, IDTO):
    __tablename__ = "Info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    weather_station_id = Column(Integer, ForeignKey("WeatherStation.id"), nullable=False)
    _date = Column(DateTime)
    temperature = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)

    weather_station = db.relationship("WeatherStation", backref="info")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "weather_station_id": self.weather_station_id,
            "date": self._date,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": self.pressure
        }

    @staticmethod
    def create_from_dto(_dict: Dict[str, Any]) -> object:
        weather_station_id = db.session.query(WeatherStation).filter(
            WeatherStation.mac_address == _dict.get("mac_address")
        ).first().id

        date = datetime.now()
        formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")

        data = {
            "weather_station_id": weather_station_id,
            "_date": formatted_date,
            "temperature": _dict["t"],
            "humidity": _dict["h"],
            "pressure": _dict["p"]
        }

        return Info(**data)
