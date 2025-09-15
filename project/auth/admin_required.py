from http import HTTPStatus
from flask import make_response, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
import functools

def admin_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()

        if not claims['is_admin']:
            return make_response(jsonify({'message': 'Only admins'}), HTTPStatus.FORBIDDEN)

        return func(*args, **kwargs)
    return wrapper
