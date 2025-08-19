from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from project.auth.admin_required import admin_required
from project.ORM.controller import weather_station_controller
from project.ORM.domain.orders.weather_station import WeatherStation

weather_station_bp = Blueprint("weather_station", __name__, url_prefix="/weather_station")

@weather_station_bp.get("/all")
@admin_required
def get_all_weather_stations() -> Response:
    weather_stations = weather_station_controller.get_all()
    weather_stations_dto = [weather_station.put_into_dto() for weather_station in weather_stations]
    return make_response(jsonify(weather_stations_dto), HTTPStatus.OK)

@weather_station_bp.get("/<int:weather_station_id>")
@jwt_required()
def get_weather_station_by_id(weather_station_id: int) -> Response:
    user_id = int(get_jwt_identity())
    print("Route")
    weather_station = weather_station_controller.get_by_id(weather_station_id, user_id)
    return_weather_station = weather_station.put_into_dto()
    return make_response(jsonify(return_weather_station), HTTPStatus.OK)

@weather_station_bp.get("")
@jwt_required()
def get_weather_stations_by_user_id():
    user_id = int(get_jwt_identity())
    weather_stations = weather_station_controller.get_by_user_id(user_id)
    weather_stations_dto = [weather_station.put_into_dto() for weather_station in weather_stations]
    return make_response(jsonify(weather_stations_dto), HTTPStatus.OK)

#only by microcontroller
@weather_station_bp.post("")
def create_weather_station() -> Response:
    data = request.get_json()
    new_weather_station = WeatherStation.create_from_dto(_dict=data)
    weather_station_controller.add(new_weather_station)
    return_weather_station = new_weather_station.put_into_dto()
    return make_response(jsonify(return_weather_station), HTTPStatus.CREATED)

@weather_station_bp.put("/<int:weather_station_id>")
@jwt_required()
def update_weather_station(weather_station_id: int) -> Response:
    data = request.get_json()
    user_id = int(get_jwt_identity())
    new_update_weather_station = WeatherStation.create_from_dto(_dict=data)
    weather_station_controller.update(weather_station_id, user_id, new_update_weather_station)
    return make_response(jsonify({"message": "Weather station updated"}), HTTPStatus.OK)

@weather_station_bp.delete("/<int:weather_station_id>")
@jwt_required()
def delete_weather_station(weather_station_id: int) -> Response:
    user_id = int(get_jwt_identity())
    weather_station_controller.delete(weather_station_id, user_id)
    return make_response(jsonify({"message": "Weather station deleted"}), HTTPStatus.OK)
