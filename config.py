from my import jwt_signature, my_email, mail_password

class Config:
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"
    JWT_SECRET_KEY = jwt_signature

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = my_email
    MAIL_PASSWORD = mail_password
    MAIL_DEFAULT_SENDER =my_email
