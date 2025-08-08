import jwt
import logging
from http import HTTPStatus
from flask import Blueprint, request, jsonify, make_response, Response, abort
from project.ORM.domain.orders.user import User
from project.auth.jwt_utils import create_jwt, create_access_token, decode_jwt
from my import jwt_signature

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post('/login')
def login() -> Response:
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.verify_password(data['password']):
        tokens = create_jwt(user.id)
        return make_response(jsonify(tokens), HTTPStatus.OK)
    return make_response(jsonify({'message': 'Invalid email or password'}), HTTPStatus.BAD_REQUEST)

@auth_bp.post('/refresh')
def refresh() -> Response:
    data = request.get_json()
    refresh_token = data['refresh_token']

    try:
        payload = jwt.decode(refresh_token, jwt_signature, algorithms=['HS256'])

        if payload is None:
            raise jwt.InvalidTokenError('Invalid refresh token')

        user_id = decode_jwt(refresh_token)
        new_access_token = create_access_token(user_id)

        return make_response(jsonify({'access_token': new_access_token}), HTTPStatus.OK)
    except jwt.ExpiredSignatureError as ex:
        logging.warning(ex)
        abort(401)
    except jwt.InvalidTokenError as ex:
        logging.warning(ex)
        abort(500) # 404
