from flask import abort

from project.ORM.domain.orders.weather_station import WeatherStation
from project.ORM.service import get_max_min_temperature_service
import logging


def check_access(obj_id: int, user_id: int) -> bool:
    users_weather_station = WeatherStation.query.filter(WeatherStation.user_id == user_id).all()
    for weather_station in users_weather_station:
        if weather_station.id == obj_id:
            return True
    return False

class GetMaxMinTemperatureController:
    _service = get_max_min_temperature_service
    _logger = logging.getLogger(__name__)

    def activate(self, weather_station_id: int, user_id: int) -> dict:
        if not check_access(weather_station_id, user_id):
            self._logger.warning(f"User (id = {user_id}) does not have access to WeatherStation (id = {weather_station_id})")
            abort(403)
        try:
            max_min_temperature = self._service.activate(weather_station_id)
            return max_min_temperature
        except Exception as ex:
            logging.error(ex)
            abort(500)
