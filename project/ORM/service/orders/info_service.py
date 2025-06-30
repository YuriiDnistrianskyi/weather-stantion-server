from project.ORM.service.general_service import GeneralService
from project.ORM.dao import info_dao
from project.ORM.domain.orders.info import Info

class InfoService(GeneralService):
    _dao = info_dao
    _class_type = Info
