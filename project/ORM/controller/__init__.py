from project.ORM.controller.orders.user_controller import UserController
from project.ORM.controller.orders.group_controller import GroupController
from project.ORM.controller.orders.user_group_controller import UserGroupController
from project.ORM.controller.orders.weather_station_controller import WeatherStationController
from project.ORM.controller.orders.info_controller import InfoController
from project.ORM.controller.orders.get_max_min_temperature_controller import GetMaxMinTemperatureController

user_controller = UserController()
group_controller = GroupController()
user_group_controller = UserGroupController()
weather_station_controller = WeatherStationController()
info_controller = InfoController()
get_max_min_temperature_controller = GetMaxMinTemperatureController()
