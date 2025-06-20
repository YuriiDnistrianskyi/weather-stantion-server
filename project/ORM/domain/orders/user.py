from sqlalchemy import Column, Integer, String
from typing import Dict, Any
from project import db
from project.ORM.domain.i_dto import IDTO

class User(db.Model, IDTO):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def put_into_dto(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
        }

    @staticmethod
    def create_from_dto(self, dict: Dict[str, Any]) -> object:
        return User(first_name=dict["first_name"], last_name=dict["last_name"], email=dict["email"], password=dict["password"])
