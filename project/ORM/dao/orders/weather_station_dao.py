from typing import List
from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.weather_station import WeatherStation
from project.ORM.domain.orders.user import User
from project.Exceptions.NotFoundException import NotFoundException

class WeatherStationDAO(GeneralDAO):
    _domain_type = WeatherStation

    def get_by_user_id(self, user_id: int) -> List[WeatherStation]:
        user = self._session.query(User).filter(User.id == user_id).first()
        if user is None:
            raise NotFoundException('User does not exist')
        weather_stations = self._session.query(WeatherStation).filter(WeatherStation.user_id == user_id).all()
        return weather_stations
