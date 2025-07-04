from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from project.ORM.controller import group_controller
from project.ORM.domain.orders.group import Group

group_bp = Blueprint("group", __name__, url_prefix="/group")

@group_bp.get("")
def get_groups() -> Response:
    groups = group_controller.get_all()
    groups_dto = [group.put_into_dto() for group in groups]
    return make_response(jsonify(groups_dto), HTTPStatus.OK)

@group_bp.get("/<int:group_id>")
def get_group(group_id: int) -> Response:
    group = group_controller.get_by_id(group_id)
    return_group = group.put_into_dto()
    return make_response(jsonify(return_group), HTTPStatus.OK)

@group_bp.post("")
def create_group() -> Response:
    data = request.get_json()
    new_group = Group.create_from_dto(_dict=data)
    group_controller.add(new_group)
    return_group = new_group.put_into_dto()
    return make_response(jsonify(return_group), HTTPStatus.CREATED)

@group_bp.put("/<int:group_id>")
def update_group(group_id: int) -> Response:
    data = request.get_json()
    new_update_group = Group.create_from_dto(_dict=data)
    group_controller.update(group_id, new_update_group)
    return make_response(jsonify({"message": "Group updated"}), HTTPStatus.OK)

@group_bp.delete("/<int:group_id>")
def delete_group(group_id: int) -> Response:
    group_controller.delete(group_id)
    return make_response(jsonify({"message": "Group deleted"}), HTTPStatus.OK)
