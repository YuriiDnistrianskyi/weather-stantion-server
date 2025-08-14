from flask import abort
from http import HTTPStatus
from project import db
from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import user_service
from project.ORM.domain.orders.user import User
from project.Exceptions.Exceptions import UserIsExistException, NotFoundException

class UserController(GeneralController):
    _service = user_service
    _class_type = User

    def get_by_id(self, user_id: int, user_id_jwt: int) -> _class_type:
        if user_id != user_id_jwt:
            abort(HTTPStatus.FORBIDDEN)
        return self._service.get_by_id(user_id)

    def add(self, obj: _class_type) -> None:
        if not obj:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)
        try:
            self._service.add(obj)
        except UserIsExistException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.CONFLICT)

    def update(self, obj_id: int, user_id: int, obj: _class_type) -> None:
        if not obj_id:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)
        if obj_id != user_id:
            abort(HTTPStatus.FORBIDDEN)
        try:
            self._service.update(obj_id, obj)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.NOT_FOUND)

    def delete(self, obj_id: int, user_id: int) -> None:
        if obj_id != user_id:
            abort(HTTPStatus.FORBIDDEN)
        try:
            self._service.delete(obj_id)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.NOT_FOUND)
