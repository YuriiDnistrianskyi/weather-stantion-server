from project.ORM.controller.general_controller import GeneralController
from project.ORM.service import info_service
from project.ORM.domain.orders.info import Info

class InfoController(GeneralController):
    _service = info_service
    _class_type = Info
