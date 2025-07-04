from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from project.ORM.controller import info_controller
from project.ORM.domain.orders.info import Info

info_bp = Blueprint("info", __name__, url_prefix="/info")

@info_bp.get("")
def get_all_info() -> Response:
    all_info = info_controller.get_all()
    all_info_dto = [info.put_into_dto() for info in all_info]
    return make_response(jsonify(all_info_dto), HTTPStatus.OK)

@info_bp.get("/<int:info_id>")
def get_info(info_id: int) -> Response:
    info = info_controller.get_by_id(info_id)
    return_info = info.put_into_dto()
    return make_response(jsonify(return_info), HTTPStatus.OK)

@info_bp.post("")
def create_info() -> Response:
    data = request.get_json()
    new_info = Info.create_from_dto(_dict=data)
    info_controller.add(new_info)
    return_info = new_info.put_into_dto()
    return make_response(jsonify(return_info), HTTPStatus.CREATED)

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
