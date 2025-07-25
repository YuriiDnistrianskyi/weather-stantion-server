from http import HTTPStatus
from datetime import datetime
from flask import Blueprint, Response, make_response, jsonify, request
from project import db
from project.ORM.controller import info_controller
from project.ORM.domain.orders.info import Info
from project.ORM.domain.orders.weather_station import WeatherStation

info_bp = Blueprint("info", __name__, url_prefix="/info")

# @info_bp.get("")
# def get_all_info() -> Response:
#     all_info = info_controller.get_all()
#     all_info_dto = [info.put_into_dto() for info in all_info]
#     return make_response(jsonify(all_info_dto), HTTPStatus.OK)

@info_bp.get("/<int:info_id>")
def get_info(info_id: int) -> Response:
    info = info_controller.get_by_id(info_id)
    return_info = info.put_into_dto()
    return make_response(jsonify(return_info), HTTPStatus.OK)

@info_bp.get("/all") #
def get_all_info_by_weather_station() -> Response:
    weather_station_id = request.args.get("weather_station_id")
    info_list = info_controller.get_all_by_weather_station_id(weather_station_id)
    return_info = [info.put_into_dto() for info in info_list]
    return make_response(jsonify(return_info), HTTPStatus.OK)

@info_bp.get("")
def get_info_by_weather_station() -> Response:
    weather_station_id = request.args.get("weather_station_id")
    info = info_controller.get_by_weather_station_id(weather_station_id)
    return_info = info.put_into_dto()
    return make_response(jsonify(return_info), HTTPStatus.OK)

@info_bp.post("")
def create_info() -> Response:
    data_request = request.get_json()

    weather_station_id = db.session.query(WeatherStation).filter(WeatherStation.mac_address == data_request["mac_address"]).first().id

    date = datetime.now()
    formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "weather_station_id": weather_station_id,
        "_date": formatted_date,
        "temperature": data_request["t"],
        "humidity": data_request["h"],
        "pressure": data_request["p"]
    }

    new_info = Info.create_from_dto(_dict=data)
    info_controller.add(new_info)
    return_info = new_info.put_into_dto()
    return make_response(jsonify(return_info), HTTPStatus.OK)

@info_bp.put("/<int:info_id>")
def update_info(info_id: int) -> Response:
    data = request.get_json()
    new_update_info = Info.create_from_dto(_dict=data)
    info_controller.update(info_id, new_update_info)
    return make_response(jsonify({"message": "Information updated"}), HTTPStatus.OK)

@info_bp.delete("/<int:info_id>")
def delete_info(info_id: int) -> Response:
    info_controller.delete(info_id)
    return make_response(jsonify({"message": "Information deleted"}), HTTPStatus.OK)
