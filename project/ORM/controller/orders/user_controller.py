from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import user_service
from project.ORM.domain.orders.user import User

class UserController(GeneralController):
    _service = user_service
    _class_type = User
