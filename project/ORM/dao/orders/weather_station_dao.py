from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.weather_station import WeatherStation

class WeatherStationDAO(GeneralDAO):
    _domain_type = WeatherStation
