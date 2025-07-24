from http import HTTPStatus
from flask import Blueprint, make_response, jsonify, Response
from project.ORM.controller import get_max_min_temperature_controller

get_max_min_temperature_bp = Blueprint("get_max_min_temperature", __name__, url_prefix="/get_max_min_temperature")

@get_max_min_temperature_bp.get("")
def get_max_min_temperature() -> Response:
    max_min_temperature = get_max_min_temperature_controller.activate()
    return make_response(jsonify(max_min_temperature), HTTPStatus.OK)
