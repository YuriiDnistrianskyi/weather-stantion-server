from typing import List
from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.info import Info
from project.ORM.domain.orders.weather_station import WeatherStation
from project.Exceptions.NotFoundException import NotFoundException

class InfoDAO(GeneralDAO):
    _domain_type = Info

    def get_all_by_weather_station_id(self, weather_station_id: str) -> List[Info]:
        weather_station = self._session.query(WeatherStation).filter(WeatherStation.id == weather_station_id).first()
        if weather_station is None:
            raise NotFoundException(f'Weather station not found (id = {weather_station_id})')
        data_list = self._session.query(Info).filter(Info.weather_station_id == weather_station_id).all()
        return data_list

    def get_by_weather_station_id(self, weather_station_id: int) -> _domain_type:
        weather_station = self._session.query(WeatherStation).filter(WeatherStation.id == weather_station_id).first()
        if weather_station is None:
            raise NotFoundException(f'Weather station not found (id = {weather_station_id})')
        # data = self._session.query(Info).filter(Info.weather_station_id == weather_station_id).first()

        data_list = self._session.query(Info).filter(Info.weather_station_id == weather_station_id).all()
        current_data = data_list[0]
        for data in data_list:
            if data._date > current_data._date:
                current_data = data
        return current_data

        # return data
