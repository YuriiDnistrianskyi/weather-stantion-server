from project.ORM.dao.orders.user_dao import UserDAO
from project.ORM.dao.orders.group_dao import GroupDAO
from project.ORM.dao.orders.user_group_dao import UserGroupDAO
from project.ORM.dao.orders.weather_station_dao import WeatherStationDAO
from project.ORM.dao.orders.info_dao import InfoDAO
from project.ORM.dao.orders.get_max_min_temperature_dao import GetMaxMinTemperatureDao

user_dao = UserDAO()
group_dao = GroupDAO()
user_group_dao = UserGroupDAO()
weather_station_dao = WeatherStationDAO()
info_dao = InfoDAO()
get_max_min_temperature_dao = GetMaxMinTemperatureDao()
