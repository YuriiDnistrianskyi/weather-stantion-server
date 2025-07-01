from sqlalchemy import Column, Integer, String, ForeignKey
from typing import Dict, Any
from project import db
from project.ORM.domain.i_dto import IDTO

class WeatherStation(db.Model, IDTO):
    __tablename__ = "WeatherStation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    mac_address = Column(String(50))
    name = Column(String(50))
    location = Column(String(50))
    user_id = Column(Integer, ForeignKey("User.id"))
    group_id = Column(Integer, ForeignKey("Group.id"))

    group = db.relationship("Group", back_populates="weather_station", uselist=False)
    owner = db.relationship("User", backref="weather_stations")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "mac_address": self.mac_address,
            "name": self.name,
            "location": self.location,
            "user": self.owner.put_into_dto() if self.owner is not None else None,
            "group": self.group.put_into_dto() if self.group is not None else None
        }

    @staticmethod
    def create_from_dto(_dict: Dict[str, Any]) -> object:
        return WeatherStation(mac_address=_dict["mac_address"], name=_dict["name"], location=_dict["location"], user_id=_dict["user_id"], group_id=_dict["group_id"])
