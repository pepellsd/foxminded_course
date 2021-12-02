from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import Configuration


def create_app(test_config=None):
    application = Flask(__name__)
    application.config.from_object(Configuration)
    if test_config:
        application.config.update(test_config)
    return application


app = create_app()
api = Api(app)
db = SQLAlchemy(app)