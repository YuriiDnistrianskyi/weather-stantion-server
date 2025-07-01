from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import user_group_service
from project.ORM.domain.orders.user_group import UserGroup

class UserGroupController(GeneralController):
    _service = user_group_service
    _class_type = UserGroup

    def get_by_id(self, user_id: int, group_id: int) -> _class_type:
        return self._service.get_by_id(user_id, group_id)

    def update(self, user_id: int, group_id: int, new_user_group: _class_type) -> None:
        self._service.update(user_id, group_id, new_user_group)

    def delete(self, user_id: int, group_id: int) -> None:
        self._service.delete(user_id, group_id)
