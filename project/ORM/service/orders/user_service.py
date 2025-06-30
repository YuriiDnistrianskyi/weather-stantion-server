from project.ORM.service.general_service import GeneralService
from project.ORM.dao import user_dao
from project.ORM.domain.orders.user import User

class UserService(GeneralService):
    _dao = user_dao
    _class_type = User
