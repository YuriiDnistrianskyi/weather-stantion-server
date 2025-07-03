from sqlalchemy import inspect
from sqlalchemy.orm import Mapper

from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.user_group import UserGroup

class UserGroupDAO(GeneralDAO):
    _domain_type = UserGroup

    def get_by_id(self, user_id: int, group_id: int) -> _domain_type:
        return self._session.query(UserGroup).filter(UserGroup.user_id == user_id, UserGroup.group_id == group_id).first()

    def update(self, user_id: int, group_id: int, new_user_group: _domain_type) -> None:
        old_user_group = self._session.query(UserGroup).filter(UserGroup.user_id == user_id, UserGroup.group_id == group_id).first()
        mapper: Mapper = inspect(type(new_user_group))
        columns = mapper.columns.items()
        for column_name, column_obj in columns:
            value = getattr(new_user_group, column_name)
            setattr(old_user_group, column_name, value)
        self._session.commit()

    def delete(self, user_id: int, group_id: int) -> None:
        delete_user_group = self._session.query(UserGroup).filter(UserGroup.user_if == user_id, UserGroup.group_id == group_id).first()
        self._session.delete(delete_user_group)
        try:
            self._session.commit()
        except:
            self._session.rollback()
            raise
