from sqlalchemy import Column, Integer, String
from typing import Dict, Any
from project import db
from project.ORM.domain.i_dto import IDTO
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, IDTO):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)

    # weather_stations = db.relationship("WeatherStation", back_populates="owner")
    # groups = db.relationship("Group", secondary="UserGroup", back_populates="users")

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def put_into_dto(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": "hash"
        }

    @staticmethod
    def create_from_dto(_dict: Dict[str, Any]) -> object:
        return User(**_dict)
