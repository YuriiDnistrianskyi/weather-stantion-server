from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from project.ORM.controller import user_controller
from project.ORM.domain.orders.user import User

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.get("")
def get_users() -> Response:
    users = user_controller.get_all()
    users_dto = [user.put_into_dto() for user in users]
    return make_response(jsonify(users_dto), HTTPStatus.OK)

@user_bp.get("/<int:user_id>")
def get_user(user_id: int) -> Response:
    user = user_controller.get_by_id(user_id)
    return_user = user.put_into_dto()
    return make_response(jsonify(return_user), HTTPStatus.OK)

@user_bp.post("")
def create_user() -> Response:
    data = request.get_json()
    print(type(data))
    new_user = User.create_from_dto(_dict=data)
    user_controller.add(new_user)
    return_user = new_user.put_into_dto()
    return make_response(jsonify(return_user), HTTPStatus.CREATED)

@user_bp.put("/<int:user_id>")
def update_user(user_id: int) -> Response:
    data = request.get_json()
    new_update_user = User.create_from_dto(_dict=data)
    user_controller.update(user_id, new_update_user)
    return make_response(jsonify({"message": "User updated"}), HTTPStatus.OK)

@user_bp.delete("/<int:user_id>")
def delete_user(user_id: int) -> Response:
    user_controller.delete(user_id)
    return make_response(jsonify({"message": "User deleted"}), HTTPStatus.OK)
