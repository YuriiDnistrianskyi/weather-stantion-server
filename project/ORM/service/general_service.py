from typing import List
from project import db

class GeneralService:
    _dao = None
    _class_type = None
    _session = db.session

    def get_all(self) -> List[_class_type]:
        return self._dao.get_all()

    def get_by_id(self, obj_id: int) -> _class_type:
        return self._dao.get_by_id(obj_id)

    def add(self, obj: _class_type) -> None:
        self._dao.add(obj)

    def update(self, obj_id: int, obj: _class_type) -> None:
        self._dao.update(obj_id, obj)

    def delete(self, obj_id: int) -> None:
        self._dao.delete(obj_id)
