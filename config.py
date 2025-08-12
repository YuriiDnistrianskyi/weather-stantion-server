from my import jwt_signature

class Config:
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"
    JWT_SECRET_KEY = jwt_signature
