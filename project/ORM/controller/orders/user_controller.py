from flask import abort
from http import HTTPStatus
from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import user_service
from project.ORM.domain.orders.user import User
from project.Exceptions.UserIsExistsException import UserIsExistException

class UserController(GeneralController):
    _service = user_service
    _class_type = User

    def add(self, obj: _class_type) -> None:
        if not obj:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)
        try:
            self._service.add(obj)
        except UserIsExistException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.CONFLICT)
