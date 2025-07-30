import jwt
import datetime
from flask import current_app
from my import jwt_signature

def create_jwt(user_id: int) -> str:
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    return jwt.encode(payload, jwt_signature, algorithm='HS256') # current_app.config['JWT_SECRET']

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, jwt_signature, algorithms=['HS256']) # current_app.config['JWT_SECRET']
        return payload['user_id']
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None

