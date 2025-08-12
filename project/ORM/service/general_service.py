from typing import List
from project import db
from project.Exceptions.Exceptions import ForbiddenAccessException

class GeneralService:
    _dao = None
    _class_type = None
    _session = db.session

    def get_all(self) -> List[_class_type]:
        return self._dao.get_all()

    def get_by_id(self, obj_id: int) -> _class_type:
        return self._dao.get_by_id(obj_id)

    # for User other method
    # def get_by_id(self, obj_id: int, user_id: int) -> _class_type:
    #     users_weather_station = db.session.query(self._class_type).filter(self._class_type.user_id == user_id).all()
    #     for weather_station in users_weather_station:
    #         if weather_station.id == obj_id:
    #             return self._dao.get_by_id(obj_id)
    #     raise ForbiddenAccessException(f"User (id = {user_id}) does not have access to {self._c;ass_type} (id = {obj_id})")

    def add(self, obj: _class_type) -> None:
        self._dao.add(obj)

    def update(self, obj_id: int, obj: _class_type) -> None:
        self._dao.update(obj_id, obj)

    def delete(self, obj_id: int) -> None:
        self._dao.delete(obj_id)
