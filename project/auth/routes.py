from http import HTTPStatus
from flask import request, jsonify, make_response, Response
from project.ORM.domain.orders.user import User
from project.auth import auth_bp
from project.auth.jwt_utils import create_jwt

@auth_bp.post('/login')
def login() -> Response:
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.verify_password(data['password']):
        token = create_jwt(user.id)
        return make_response(jsonify({'token': token}), HTTPStatus.OK)
    return make_response(jsonify({'message': 'Invalid email or password'}), HTTPStatus.BAD_REQUEST)

# @auth_bp.get('/logout')
# def logout() -> Response:
#     return make_response(jsonify({'message': 'Logged out'}), HTTPStatus.OK)
