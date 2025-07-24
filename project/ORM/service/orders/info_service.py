from project.ORM.service.general_service import GeneralService
from project.ORM.dao import info_dao
from project.ORM.domain.orders.info import Info
from typing import List

class InfoService(GeneralService):
    _dao = info_dao
    _class_type = Info

    def get_all_by_weather_station_id(self, weather_station_id: int) -> List[_class_type]:
        return self._dao.get_all_by_weather_station_id(weather_station_id)

    def get_by_weather_station_id(self, weather_station_id: int) -> _class_type:
        return self._dao.get_by_weather_station_id(weather_station_id)
