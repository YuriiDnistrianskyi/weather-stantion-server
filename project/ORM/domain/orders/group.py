from sqlalchemy import Column, Integer, String, ForeignKey
from typing import Dict, Any
from project import db
from project.ORM.domain.i_dto import IDTO

class Group(db.Model, IDTO):
    __tablename__ = "Group"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    owner_id = Column(Integer, ForeignKey("User.id"))

    weather_station = db.relationship("WeatherStation", back_populates="group", uselist=False)
    users = db.relationship("User", secondary="UserGroup", back_populates="groups")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
            "station": self.weather_station,
        }

    @staticmethod
    def create_from_dto(_dict: Dict[str, Any]) -> object:
        return Group(name=_dict["name"], owner_id=_dict["owner_id"])
