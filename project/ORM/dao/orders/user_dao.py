from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.user import User

class UserDAO(GeneralDAO):
    __domain_type = User
