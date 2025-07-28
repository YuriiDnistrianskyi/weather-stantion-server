from project.ORM.service.general_service import GeneralService
from project.ORM.dao import user_dao
from project.ORM.domain.orders.user import User
from project.Exceptions.UserIsExistsException import UserIsExistException

class UserService(GeneralService):
    _dao = user_dao
    _class_type = User

    def add(self, obj: _class_type) -> None:
        all_user = self._session.query(User).all()
        for user in all_user:
            if user.email == obj.email:
                raise UserIsExistException(f"User already exists (email == {obj.email})")
        self._dao.add(obj)
