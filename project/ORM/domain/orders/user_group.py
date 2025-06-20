from sqlalchemy import Column, Integer, ForeignKey
from typing import Dict, Any
from project import db
from project.ORM.domain.i_dto import IDTO

class UserGroup(db.Model, IDTO):
    __tablename__ = "UserGroup"
    user_id = Column(Integer, ForeignKey("User.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("Group.id"), primary_key=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "group_id": self.group_id,
        }

    def create_from_dto(self, _dict: Dict[str, Any]) -> object:
        return UserGroup(user_id=_dict["user_id"], group_id=_dict["group_id"])
