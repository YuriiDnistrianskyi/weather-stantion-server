from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import group_service
from project.ORM.domain.orders.group import Group

class GroupController(GeneralController):
    _service = group_service
    _class_type = Group

    def check_access(self, obj_id: int, user_id: int) -> bool:
        group = Group.query.filter(Group.id == obj_id).first()
        if group.owner_id == user_id:
            return True
        return False
