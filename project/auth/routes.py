import jwt
import logging
from http import HTTPStatus
from flask import Blueprint, request, jsonify, make_response, Response, abort
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from project.ORM.domain.orders.user import User
# from project.auth.jwt_utils import create_jwt, create_access_token, decode_jwt
from my import jwt_signature

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post('/login')
def login() -> Response:
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.verify_password(data['password']):
        access_token = create_access_token(identity=str(user.id))
        refresh_token = create_refresh_token(identity=str(user.id))
        additional_claims = {'is_admin': user.is_admin}
        return make_response(jsonify(access_token=access_token, refresh_token=refresh_token), HTTPStatus.OK)
    return make_response(jsonify({'message': 'Invalid email or password'}), HTTPStatus.BAD_REQUEST)

@auth_bp.post('/refresh')
@jwt_required(refresh=True)
def refresh() -> Response:
    user_id_str = get_jwt_identity()
    new_access_token = create_access_token(identity=user_id_str)
    return make_response(jsonify({'access_token': new_access_token}), HTTPStatus.OK)
