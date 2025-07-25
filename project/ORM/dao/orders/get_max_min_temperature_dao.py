from sqlalchemy import text
from project import db
import json

class GetMaxMinTemperatureDao:
    def activate(self) -> dict:
        max_min_temperature_json = db.session.execute(text('SELECT get_max_min_temperature();')).scalar()
        max_min_temperature = json.loads(max_min_temperature_json)
        return max_min_temperature
