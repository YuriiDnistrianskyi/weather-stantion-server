from flask import abort
from http import HTTPStatus
import logging

from project.Models.NotFoundException import NotFoundException

class GeneralController:
    _service = None
    _class_type = None
    _logger = logging.getLogger(__name__)

    def get_all(self) -> list:
        return self._service.get_all()

    def get_by_id(self, obj_id: int) -> _class_type:
        try:
            return self._service.get_by_id(obj_id)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.NOT_FOUND)

    def add(self, obj: _class_type) -> None:
        if not obj:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)
        self._service.add(obj)

    def update(self, obj_id: int, obj: _class_type) -> None:
        if not obj_id:
            abort(HTTPStatus.UNPROCESSABLE_ENTITY)
        try:
            self._service.update(obj_id, obj)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.NOT_FOUND)

    def delete(self, obj_id: int) -> None:
        try:
            self._service.delete(obj_id)
        except NotFoundException as ex:
            self._logger.warning(ex)
            abort(HTTPStatus.NOT_FOUND)
