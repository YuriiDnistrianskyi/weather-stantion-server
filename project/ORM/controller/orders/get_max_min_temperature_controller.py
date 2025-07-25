from flask import abort
from project.ORM.service import get_max_min_temperature_service
import logging

class GetMaxMinTemperatureController:
    _service = get_max_min_temperature_service
    _logger = logging.getLogger(__name__)

    def activate(self) -> dict:
        try:
            max_min_temperature = self._service.activate()
            return max_min_temperature
        except Exception as ex:
            logging.error(ex)
            abort(500)
