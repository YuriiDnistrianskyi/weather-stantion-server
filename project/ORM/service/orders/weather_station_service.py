from typing import List
from project.ORM.service.general_service import GeneralService
from project.ORM.dao import weather_station_dao
from project.ORM.domain.orders.weather_station import WeatherStation

class WeatherStationService(GeneralService):
    _dao = weather_station_dao
    _class_type = WeatherStation

    def get_by_user_id(self, user_id: int) -> List[WeatherStation]:
        return self._dao.get_by_user_id(user_id)
