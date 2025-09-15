from sqlalchemy import text
from project import db
import json

class GetMaxMinTemperatureDao:
    def activate(self, weather_station_id: int) -> dict:
        max_min_temperature_json = db.session.execute(text(f'SELECT get_max_min_temperature({weather_station_id});')).scalar()
        max_min_temperature = json.loads(max_min_temperature_json)
        return max_min_temperature
