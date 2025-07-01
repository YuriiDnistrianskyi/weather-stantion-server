from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from project.ORM.controller import user_group_controller
from project.ORM.domain.orders.user_group import UserGroup

user_group_bp = Blueprint("user_group", __name__, url_prefix="/user_group")

@user_group_bp.get("")
def get_user_groups() -> Response:
    user_groups = user_group_controller.get_all()
    user_groups_dto = [user_group.put_into_dto() for user_group in user_groups]
    return make_response(jsonify(user_groups_dto), HTTPStatus.OK)

@user_group_bp.get("/<int:user_id>/<int:group_id>")
def get_user_group(user_id: int, group_id: int) -> Response:
    user_group = user_group_controller.get_by_id(user_id, group_id)
    user_group_dto = user_group.put_into_dto()
    return make_response(jsonify(user_group_dto), HTTPStatus.OK)

@user_group_bp.post("")
def create_user_group() -> Response:
    data = request.get_json()
    new_user_group = UserGroup.create_from_dto(_dict=data)
    user_group_controller.add(new_user_group)
    user_group_dto = new_user_group.put_into_dto()
    return make_response(jsonify(user_group_dto), HTTPStatus.CREATED)

@user_group_bp.put("/<int:user_id>/<int:group_id>")
def update_user_group(user_id: int, group_id: int) -> Response:
    data = request.get_json()
    new_update_user_group = UserGroup.create_from_dto(_dict=data)
    user_group_controller.update(user_id, group_id, new_update_user_group)
    return make_response(jsonify({"massage": "UserGroup updated"}), HTTPStatus.OK)

@user_group_bp.delete("/<int:user_id>/<int:group_id>")
def delete_user_group(user_id: int, group_id: int) -> Response:
    user_group_controller.delete(user_id, group_id)
    return make_response(jsonify({"message": "UserGroup deleted"}), HTTPStatus.OK)
