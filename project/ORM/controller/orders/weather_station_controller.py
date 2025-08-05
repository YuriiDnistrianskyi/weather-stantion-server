from flask import abort
from typing import List
from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import weather_station_service
from project.ORM.domain.orders.weather_station import WeatherStation
from project.Exceptions.NotFoundException import NotFoundException

class WeatherStationController(GeneralController):
    _service = weather_station_service
    _class_type = WeatherStation

    def get_by_user_id(self, user_id: int) -> List[WeatherStation]:
        try:
            return self._service.get_by_user_id(user_id)
        except NotFoundException as ex:
            self._logger.error(ex)
            abort(404)
        except Exception as ex:
            self._logger.error(ex)
            abort(500)
