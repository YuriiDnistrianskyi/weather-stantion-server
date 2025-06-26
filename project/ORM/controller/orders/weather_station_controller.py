from project.ORM.controller.general_controller import GeneralController
from project.ORM.service.orders import weather_station_service
from project.ORM.domain.orders.weather_station import WeatherStation

class WeatherStationController(GeneralController):
    _service = weather_station_service
    _class_type = WeatherStation
