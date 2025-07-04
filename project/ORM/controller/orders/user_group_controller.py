from flask import abort
from http import HTTPStatus
from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import user_group_service
from project.ORM.domain.orders.user_group import UserGroup
from project.Models.NotFoundException import NotFoundException
from project.Models.ConflictException import ConflictException

class UserGroupController(GeneralController):
    _service = user_group_service
    _class_type = UserGroup

    def get_by_id(self, user_id: int, group_id: int) -> _class_type:
        return self._service.get_by_id(user_id, group_id)

    def add(self, obj: _class_type) -> None:
        if not obj:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)
        try:
            self._service.add(obj)
        except ConflictException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.CONFLICT)

    def update(self, user_id: int, group_id: int, new_user_group: _class_type) -> None:
        try:
            self._service.update(user_id, group_id, new_user_group)
        except NotFoundException as ex:
            self._logger.writing(ex)
            abort(HTTPStatus.NOT_FOUND)

    def delete(self, user_id: int, group_id: int) -> None:
        try:
            self._service.delete(user_id, group_id)
        except NotFoundException as ex:
            self._logger.writing(ex)
            abort(HTTPStatus.NOT_FOUND)
