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

    def check_access(self, obj_id: int, user_id: int) -> bool:
        if obj_id == user_id:
                return True
        return False
