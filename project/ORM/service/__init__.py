from project.ORM.service.orders.user_service import UserService
from project.ORM.service.orders.group_service import GroupService
from project.ORM.service.orders.user_group_sevice import UserGroupService
from project.ORM.service.orders.weather_station_service import WeatherStationService
from project.ORM.service.orders.info_service import InfoService
from project.ORM.service.orders.get_max_min_temperature_service import GetMaxMinTemperatureService

user_service = UserService()
group_service = GroupService()
user_group_service = UserGroupService()
weather_station_service = WeatherStationService()
info_service = InfoService()
get_max_min_temperature_service = GetMaxMinTemperatureService()
