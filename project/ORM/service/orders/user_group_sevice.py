from project.ORM.service.general_service import GeneralService
from project.ORM.dao.orders import user_group_dao
from project.ORM.domain.orders.user_group import UserGroup

class UserGroupService(GeneralService):
    _dao = user_group_dao
    _class_type = UserGroup
