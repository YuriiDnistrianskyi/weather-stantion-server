from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import group_service
from project.ORM.domain.orders.group import Group

class GroupController(GeneralController):
    _service = group_service
    _class_type = Group
