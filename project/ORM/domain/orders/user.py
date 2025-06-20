from sqlalchemy import Column, Integer, String
from typing import Dict, Any
from project import db
from project.ORM.domain.i_dto import IDTO

class User(db.Model, IDTO):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    weather_stations = db.relationship("WeatherStation", back_populates="owner")
    groups = db.relationship("Group", secondary="UserGroup", back_populates="users")

    def put_into_dto(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def create_from_dto(self, _dict: Dict[str, Any]) -> object:
        return User(first_name=_dict["first_name"], last_name=_dict["last_name"], email=_dict["email"], password=_dict["password"])
