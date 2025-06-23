from project.ORM.service.general_service import GeneralService
from project.ORM.dao.orders import group_dao
from project.ORM.domain.orders.group import Group

class GroupService(GeneralService):
    _dao = group_dao
    _class_type = Group
