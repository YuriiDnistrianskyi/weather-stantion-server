from flask import abort
from typing import List
from project.ORM.controller.general_controller import GeneralController
from project.ORM.domain.orders.weather_station import WeatherStation
from project.ORM.service import info_service
from project.ORM.domain.orders.info import Info
from project.Exceptions.NotFoundException import NotFoundException

class InfoController(GeneralController):
    _service = info_service
    _class_type = Info

    def check_access(self, obj_id: int, user_id: int) -> bool:
        info = Info.query.filter_by(id=obj_id).first()
        if info is None:
            abort(404)
        weather_station = WeatherStation.query.filter_by(id=info.weather_station_id, user_id=user_id).first()
        if weather_station is None:
            return False
        return True

    def get_all_by_weather_station_id(self, weather_station_id, user_id: int) -> List[_class_type]:
        weather_station = WeatherStation.query.filter_by(id=weather_station_id, user_id=user_id).first()
        if weather_station is not None:
            try:
                return self._service.get_all_by_weather_station_id(weather_station_id)
            except NotFoundException as ex:
                self._logger.exception(ex)
                abort(404)
        self._logger.warning(f"User (id = {user_id}) does not have access to WeatherStation (Data) (id = {weather_station_id})")
        abort(403)

    def get_by_weather_station_id(self, weather_station_id: int, user_id: int) -> _class_type:
        weather_station = WeatherStation.query.filter_by(id=weather_station_id, user_id=user_id).first()
        if weather_station is not None:
            try:
                return self._service.get_by_weather_station_id(weather_station_id)
            except NotFoundException as ex:
                self._logger.exception(ex)
                abort(404)
        self._logger.warning(f"User (id = {user_id}) does not have access to WeatherStation (Data) (id = {weather_station_id})")
        abort(403)
