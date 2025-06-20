from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from my import db_password

db = SQLAlchemy()

def create_app() -> Flask:
    app = Flask(__name__)
    init_db(app)
    return app

def init_db(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{db_password}@127.0.0.1:3306/WeatherStation"

    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        print("Create database")

    db.init_app(app)

    import project.ORM.domain
    with app.app_context():
        db.create_all()
        print("Create tables")
