from typing import List
from project import db
from project.ORM.service.general_service import GeneralService
from project.ORM.dao import weather_station_dao
from project.ORM.domain.orders.weather_station import WeatherStation
from project.ORM.domain.orders.user import User
from project.Exceptions.NotFoundException import NotFoundException
from project.Exceptions.ConflictException import ConflictException

class WeatherStationService(GeneralService):
    _dao = weather_station_dao
    _class_type = WeatherStation

    def get_by_user_id(self, user_id: int) -> List[WeatherStation]:
        return self._dao.get_by_user_id(user_id)

    def add(self, obj: WeatherStation) -> None:
        user = db.session.query(User).filter_by(id=obj.user_id).first()
        if user is None:
            raise NotFoundException(f"User does not exists (id = {obj.user_id})")
        weather_stations = db.session.query(WeatherStation).all()
        for weather_station in weather_stations:
            if obj.mac_address == weather_station.mac_address:
                raise ConflictException("weather station already exists (mac_address)")
        # create group
        return self._dao.create(obj)
