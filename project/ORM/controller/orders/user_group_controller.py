from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import user_group_service
from project.ORM.domain.orders.user_group import UserGroup

class UserGroupController(GeneralController):
    _service = user_group_service
    _class_type = UserGroup
