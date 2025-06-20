from sqlalchemy import Column, Integer, String, ForeignKey,
from typing import Dict, Any
from project import db
from project.ORM.domain.i_dto import IDTO

class Info(db.Model, IDTO):
    __tablename__ = "info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    weather_station_id = Column(Integer, ForeignKey("weather_stations.id"), nullable=False)
    date = Column(String)
    temperature = Column(Integer)
    humidity = Column(Integer)
    CO2 = Column(Integer)

    # weather_station = db.relationship("WeatherStation", back_populates="info")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "weather_station_id": self.weather_station_id,
            "date": self.date,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "CO2": self.CO2,
        }

    @staticmethod
    def create_from_dto(dto: Dict[str, Any]) -> object:
        return Info(weather_station_id=dict["weather_station_id"], date=dict["date"], temperature=dict["temperature"], humidity=dict["humidity"], CO2=dict["CO2"])
