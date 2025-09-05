from typing import List
from project import db
from project.ORM.service.general_service import GeneralService
from project.ORM.dao import info_dao
from project.ORM.domain.orders.info import Info
from project.ORM.domain.orders.weather_station import WeatherStation
from project.ORM.domain.orders.user import User
from project.email.emails_for_data import *

class InfoService(GeneralService):
    _dao = info_dao
    _class_type = Info

    def get_all_by_weather_station_id(self, weather_station_id: int) -> List[_class_type]:
        return self._dao.get_all_by_weather_station_id(weather_station_id)

    def get_by_weather_station_id(self, weather_station_id: int) -> _class_type:
        return self._dao.get_by_weather_station_id(weather_station_id)

    def add(self, obj: _class_type) -> None:
        weather_station = db.session.query(WeatherStation).filter_by(id=obj.weather_station_id).first()
        user_email = db.session.query(User).filter_by(id=weather_station.user_id).first().email

        if obj.temperature > 40:
            exceeding_temperature(user_email, weather_station.name, obj.temperature)
        elif obj.temperature < -20:
            exceeding_low_temperature(user_email, weather_station.name, obj.temperature)

        # can add humidity control

        self._dao.add(obj)
