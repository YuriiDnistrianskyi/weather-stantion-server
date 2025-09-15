from flask import abort
from typing import List
from project import db
from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import weather_station_service
from project.ORM.domain.orders.weather_station import WeatherStation
from project.Exceptions.NotFoundException import NotFoundException

class WeatherStationController(GeneralController):
    _service = weather_station_service
    _class_type = WeatherStation

    def check_access(self, obj_id: int, user_id: int) -> bool:
        users_weather_station = db.session.query(self._class_type).filter(self._class_type.user_id == user_id).all()
        for weather_station in users_weather_station:
            if weather_station.id == obj_id:
                return True
        return False

    def get_by_user_id(self, user_id: int) -> List[WeatherStation]:
        try:
            return self._service.get_by_user_id(user_id)
        except NotFoundException as ex:
            self._logger.error(ex)
            abort(404)
        except Exception as ex:
            self._logger.error(ex)
            abort(500)
