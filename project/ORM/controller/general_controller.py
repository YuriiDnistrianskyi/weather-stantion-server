from flask import abort
from http import HTTPStatus
import logging
from project.Exceptions.Exceptions import NotFoundException, ConflictException, ForbiddenAccessException, UserIsExistException

class GeneralController:
    _service = None
    _class_type = None
    _logger = logging.getLogger(__name__)

    def check_access(self, obj_id: int, user_id: int) -> bool:
        self._logger.info("Use default check_access method in controller")
        return False

    def get_all(self) -> list:
        return self._service.get_all()

    def get_by_id(self, obj_id: int, user_id: int) -> _class_type:
        # if user_id is not None:
        try:
            if not self.check_access(obj_id, user_id):
                self._logger.warning(f"User (id = {user_id}) does not have access to {self._class_type} (id = {obj_id})")
                abort(403)
            return self._service.get_by_id(obj_id)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(404)

    def add(self, obj: _class_type) -> None:
        if not obj:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)
        try:
            self._service.add(obj)
        except ConflictException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.CONFLICT)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.NOT_FOUND)
        except UserIsExistException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.CONFLICT)

    def update(self, obj_id: int, user_id: int, obj: _class_type) -> None:
        if not obj_id:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)
        if not self.check_access(obj_id, user_id):
            self._logger.warning(f"User (id = {user_id}) does not have access to {self._class_type} (id = {obj_id})")
            abort(403)
        try:
            self._service.update(obj_id, obj)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.NOT_FOUND)

    def delete(self, obj_id: int, user_id: int) -> None:
        if not self.check_access(obj_id, user_id):
            self._logger.warning(f"User (id = {user_id}) does not have access to {self._class_type} (id = {obj_id})")
            abort(403)
        try:
            self._service.delete(obj_id)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.NOT_FOUND)
