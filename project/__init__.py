from flask import Flask
from flask_jwt_extended import JWTManager
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from sqlalchemy_utils import database_exists, create_database
from .route import register_routes
from my import db_password
import os
from config import Config

db = SQLAlchemy()
mail = Mail()

import logging

logging.basicConfig(
    level=logging.INFO,  # або INFO
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    jwt = JWTManager(app) #

    mail.init_app(app)

    init_db(app)
    create_db_functions(app)
    register_routes(app)

    return app

def init_db(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{db_password}@127.0.0.1:3306/WeatherStation"

    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        logging.info("Database created successfully")

    db.init_app(app)

    import project.ORM.domain
    with app.app_context():
        db.create_all()
        logging.info("Tables created successfully")

def create_db_functions(app: Flask) -> None:
    with app.app_context():
        path_files = os.path.join(os.path.dirname(__file__), 'db', 'functions')
        function_files = ['get_max_min_temperature.sql']

        for function_file in function_files:
            with open(os.path.join(path_files, function_file), 'r', encoding='utf-8') as file:
                file_content = file.read()
            drop_part, create_part = file_content.split('CREATE', 1)

            db.session.execute(text(drop_part))
            db.session.execute(text('CREATE' + create_part))
            db.session.commit()

        logging.info("Functions created successfully")
