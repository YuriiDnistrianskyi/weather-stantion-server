from sqlalchemy import text
from project import db

class GetMaxMinTemperatureDao:
    def activate(self):
        max_min_temperature = db.session.execute(text('SELECT get_max_min_temperature();')).scalar()
        print(max_min_temperature)
        print(type(max_min_temperature))
        return max_min_temperature
