from abc import ABC
from typing import List
from project import db #
from sqlalchemy import inspect
from sqlalchemy.orm import Mapper

class GeneralDAO(ABC):
    _domain_type = None
    _session = db.session

    def get_all(self) -> List[_domain_type]:
        return self._session.query(self._domain_type).all()

    def get_by_id(self, obj_id: int) -> _domain_type:
        return self._session.query(self._domain_type).filter_by(id=obj_id).first()

    def add(self, obj: _domain_type) -> None:
        self._session.add(obj)
        self._session.commit()

    def update(self, obj_id: int, obj: _domain_type) -> None:
        domain_obj = self._session.query(self._domain_type).filter_by(id=obj_id).first()
        mapper: Mapper = inspect(type(obj))
        columns = mapper.columns.items()
        for column_name, column_obj in columns:
            if not column_obj.primaty_key:
                value = getattr(obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()

    def delete(self, obj_id: int) -> None :
        domain_obj = self._session.query(self._domain_type).filter_by(id=obj_id).first()
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
