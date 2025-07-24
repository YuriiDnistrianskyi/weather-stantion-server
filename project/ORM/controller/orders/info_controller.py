from flask import abort
from typing import List
from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import info_service
from project.ORM.domain.orders.info import Info

class InfoController(GeneralController):
    _service = info_service
    _class_type = Info

    def get_all_by_weather_station_id(self, weather_station_id) -> List[_class_type]:
        try:
            return self._service.get_all_by_weather_station_id(weather_station_id)
        except Exception as ex:
            self._logger.exception(ex)
            abort(500)

    def get_by_weather_station_id(self, weather_station_id) -> _class_type:
        try:
            return self._service.get_by_weather_station_id(weather_station_id)
        except Exception as ex:
            self._logger.exception(ex)
            abort(500)
