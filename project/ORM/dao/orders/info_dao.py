from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.info import Info
from typing import List

class InfoDAO(GeneralDAO):
    _domain_type = Info

    def get_all_by_weather_station_id(self, weather_station_id: str) -> List[Info]:
        data_list = self._session.query(Info).filter(Info.weather_station_id == weather_station_id).all()
        return data_list

    def get_by_weather_station_id(self, weather_station_id: int) -> _domain_type:
        data = self._session.query(Info).filter(Info.weather_station_id == weather_station_id).first()
        """
        data_list = ...
        current_data = data_list[0]
        for data in data_list:
            if data.date > current_data.date:
                current_data = data
        return current_data
        """
        return data
