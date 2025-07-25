from project.ORM.dao import get_max_min_temperature_dao

class GetMaxMinTemperatureService:
    _dao = get_max_min_temperature_dao

    def activate(self) -> dict:
        max_min_temperature = self._dao.activate()
        return max_min_temperature
