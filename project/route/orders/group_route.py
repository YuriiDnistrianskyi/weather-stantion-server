from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from project.auth.admin_required import admin_required
from project.ORM.controller import group_controller
from project.ORM.domain.orders.group import Group

group_bp = Blueprint("group", __name__, url_prefix="/group")

@group_bp.get("/all")
@admin_required
def get_groups() -> Response:
    groups = group_controller.get_all()
    groups_dto = [group.put_into_dto() for group in groups]
    return make_response(jsonify(groups_dto), HTTPStatus.OK)

@group_bp.get("/<int:group_id>")
@jwt_required()
def get_group(group_id: int) -> Response:
    user_id = int(get_jwt_identity())
    group = group_controller.get_by_id(group_id, user_id)
    return_group = group.put_into_dto()
    return make_response(jsonify(return_group), HTTPStatus.OK)

@group_bp.post("")
@jwt_required()
def create_group() -> Response:
    data = request.get_json()
    new_group = Group.create_from_dto(_dict=data)
    group_controller.add(new_group)
    return_group = new_group.put_into_dto()
    return make_response(jsonify(return_group), HTTPStatus.CREATED)

@group_bp.put("/<int:group_id>")
@jwt_required()
def update_group(group_id: int) -> Response:
    user_id = int(get_jwt_identity())
    data = request.get_json()
    new_update_group = Group.create_from_dto(_dict=data)
    group_controller.update(group_id, user_id, new_update_group)
    return make_response(jsonify({"message": "Group updated"}), HTTPStatus.OK)

@group_bp.delete("/<int:group_id>")
@jwt_required()
def delete_group(group_id: int) -> Response:
    user_id = int(get_jwt_identity())
    group_controller.delete(group_id, user_id)
    return make_response(jsonify({"message": "Group deleted"}), HTTPStatus.OK)
