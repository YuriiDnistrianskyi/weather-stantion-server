from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.user_group import UserGroup

class UserGroupDAO(GeneralDAO):
    __domain_type = UserGroup
