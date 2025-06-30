from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.user import User

class UserDAO(GeneralDAO):
    _domain_type = User
