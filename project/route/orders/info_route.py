from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from project.auth.admin_required import admin_required
from project.ORM.controller import info_controller
from project.ORM.domain.orders.info import Info

info_bp = Blueprint("info", __name__, url_prefix="/info")

@info_bp.get("/all_by_admin")
@admin_required
def get_all_info() -> Response:
    all_info = info_controller.get_all()
    all_info_dto = [info.put_into_dto() for info in all_info]
    return make_response(jsonify(all_info_dto), HTTPStatus.OK)

@info_bp.get("/<int:info_id>")
@jwt_required()
def get_info_by_id(info_id: int) -> Response:
    user_id = int(get_jwt_identity())
    info = info_controller.get_by_id(info_id, user_id)
    return_info = info.put_into_dto()
    return make_response(jsonify(return_info), HTTPStatus.OK)

@info_bp.get("/all") #
@jwt_required()
def get_all_info_by_weather_station() -> Response:
    weather_station_id = int(request.args.get("weather_station_id"))
    user_id = int(get_jwt_identity())
    info_list = info_controller.get_all_by_weather_station_id(weather_station_id, user_id)
    return_info = [info.put_into_dto() for info in info_list]
    return make_response(jsonify(return_info), HTTPStatus.OK)

@info_bp.get("")
@jwt_required()
def get_info_by_weather_station() -> Response:
    weather_station_id = int(request.args.get("weather_station_id"))
    user_id = int(get_jwt_identity())
    info = info_controller.get_by_weather_station_id(weather_station_id, user_id)
    return_info = info.put_into_dto()
    return make_response(jsonify(return_info), HTTPStatus.OK)

@info_bp.post("")
def create_info() -> Response:
    data_request = request.get_json()
    new_info = Info.create_from_dto(_dict=data_request)
    info_controller.add(new_info)
    return_info = new_info.put_into_dto()
    return make_response(jsonify(return_info), HTTPStatus.CREATED)

@info_bp.put("/<int:info_id>")
@jwt_required()
def update_info(info_id: int) -> Response:
    data = request.get_json()
    user_id = int(get_jwt_identity())
    new_update_info = Info.create_from_dto(_dict=data)
    info_controller.update(info_id, user_id, new_update_info)
    return make_response(jsonify({"message": "Information updated"}), HTTPStatus.OK)

@info_bp.delete("/<int:info_id>")
@jwt_required()
def delete_info(info_id: int) -> Response:
    user_id = int(get_jwt_identity())
    info_controller.delete(info_id, user_id)
    return make_response(jsonify({"message": "Information deleted"}), HTTPStatus.OK)
