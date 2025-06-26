from typing import List

class GeneralController:
    _service = None
    _class_type = None

    def get_all(self) -> List[_class_type]:
        return self._service.get_all()

    def get_by_id(self, obj_id: int) -> _class_type:
        return self._service.get_by_id(obj_id)

    def add(self, obj: _class_type) -> None:
        self._service.add(obj)

    def update(self, obj_id: int, obj: _class_type) -> None:
        self._service.update(obj_id, obj)

    def delete(self, obj_id: int) -> None:
        self._service.delete(obj_id)
