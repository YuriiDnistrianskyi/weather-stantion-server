from sqlalchemy import inspect
from sqlalchemy.orm import Mapper
from project.Exceptions.ConflictException import ConflictException
from project.Exceptions.NotFoundException import NotFoundException

from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.user_group import UserGroup

class UserGroupDAO(GeneralDAO):
    _domain_type = UserGroup

    def get_by_id(self, user_id: int, group_id: int) -> _domain_type:
        return self._session.query(UserGroup).filter(UserGroup.user_id == user_id, UserGroup.group_id == group_id).first()

    def add(self, obj: _domain_type) -> None:
        if self._session.query(UserGroup).filter(UserGroup.user_id == obj.user_id, UserGroup.group_id == obj.group_id).first():
            raise ConflictException(f"UserGroup (user_id = {obj.user_id}; group_id = {obj.group_id}) already exists)")
        self._session.add(obj)
        self._session.commit()

    def update(self, user_id: int, group_id: int, new_user_group: _domain_type) -> None:
        old_user_group = self._session.query(UserGroup).filter(UserGroup.user_id == user_id, UserGroup.group_id == group_id).first()
        if not old_user_group:
            raise NotFoundException(f"Not found {self._domain_type} (user_id = {user_id}; group_id = {group_id})")
        mapper: Mapper = inspect(type(new_user_group))
        columns = mapper.columns.items()
        for column_name, column_obj in columns:
            value = getattr(new_user_group, column_name)
            setattr(old_user_group, column_name, value)
        self._session.commit()

    def delete(self, user_id: int, group_id: int) -> None:
        delete_user_group = self._session.query(UserGroup).filter(UserGroup.user_if == user_id, UserGroup.group_id == group_id).first()
        if not delete_user_group:
            raise NotFoundException(f"Not found {self._domain_type} (user_id = {user_id}; group_id = {group_id})")
        self._session.delete(delete_user_group)
        try:
            self._session.commit()
        except:
            self._session.rollback()
            raise
