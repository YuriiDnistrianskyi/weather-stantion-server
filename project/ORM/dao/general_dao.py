from abc import ABC
from typing import List

from project import db
from sqlalchemy import inspect
from sqlalchemy.orm import Mapper

from project.Models.NotFoundException import NotFoundException


class GeneralDAO(ABC):
    _domain_type = None
    _session = db.session

    def get_all(self) -> List[_domain_type]:
        return self._session.query(self._domain_type).all()

    def get_by_id(self, obj_id: int) -> _domain_type:
        find_element = self._session.query(self._domain_type).filter_by(id=obj_id).first()
        if not find_element:
            raise NotFoundException(f"Not found {self._domain_type} (id={obj_id})")
        return find_element

    def add(self, obj: _domain_type) -> None:
        self._session.add(obj)
        self._session.commit()

    def update(self, obj_id: int, obj: _domain_type) -> None:
        domain_obj = self._session.query(self._domain_type).filter_by(id=obj_id).first()
        if not domain_obj:
            raise NotFoundException(f"Not found {self._domain_type} for updating")
        mapper: Mapper = inspect(type(obj))
        columns = mapper.columns.items()
        for column_name, column_obj in columns:
            if not column_obj.primary_key:
                value = getattr(obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()

    def delete(self, obj_id: int) -> None :
        domain_obj = self._session.query(self._domain_type).filter_by(id=obj_id).first()
        if not domain_obj:
            raise NotFoundException(f"Not found {self._domain_type} for deleting")
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
