from project.ORM.dao.general_dao import GeneralDAO
from project.ORM.domain.orders.info import Info

class InfoDAO(GeneralDAO):
    __domain_type = Info
