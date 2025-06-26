from project.ORM.controller.general_controller import GeneralController
from project.ORM.service.orders import user_group_sevice
from project.ORM.domain.orders.user_group import UserGroup

class UserGroupController(GeneralController):
    _service = user_group_sevice
    _class_type = UserGroup
