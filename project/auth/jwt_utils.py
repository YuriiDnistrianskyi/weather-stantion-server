import jwt
import datetime
from flask import current_app
from my import jwt_signature

def create_access_token(user_id: int) -> str:
    access_payload = {
        'user_id': user_id,
        'type': 'access',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    access_token = jwt.encode(access_payload, jwt_signature, algorithm='HS256') # current_app.config['JWT_SECRET']

    return access_token

def create_refresh_token(user_id: int) -> str:
    refresh_payload = {
        'user_id': user_id,
        'type': 'refresh',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }

    refresh_token = jwt.encode(refresh_payload, jwt_signature, algorithm='HS256')
    return refresh_token

def create_jwt(user_id: int) -> dict:
    access_token = create_access_token(user_id)
    refresh_token = create_refresh_token(user_id)
    return {'access_token': access_token, 'refresh_token': refresh_token}

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, jwt_signature, algorithms=['HS256']) # current_app.config['JWT_SECRET']
        return payload['user_id']
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None

