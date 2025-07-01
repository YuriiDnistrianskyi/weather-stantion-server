from project.ORM.service.general_service import GeneralService
from project.ORM.dao import user_group_dao
from project.ORM.domain.orders.user_group import UserGroup

class UserGroupService(GeneralService):
    _dao = user_group_dao
    _class_type = UserGroup

    def get_by_id(self, user_id:int , group_id: int) -> _class_type:
        return self._dao.get_by_id(user_id, group_id)

    def update(self, user_id: int, group_id: int, new_user_group: _class_type) -> None:
        self._dao.update(user_id, group_id, new_user_group)

    def delete(self, user_id: int, group_id: int) -> None:
        self._dao.delete(user_id, group_id)
