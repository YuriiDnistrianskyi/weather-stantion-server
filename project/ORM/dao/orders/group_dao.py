from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.group import Group

class GroupDAO(GeneralDAO):
    __domain_type = Group
