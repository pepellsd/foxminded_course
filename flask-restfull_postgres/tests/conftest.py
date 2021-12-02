import pytest
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app import create_app
from endpoints import add_urls


@pytest.fixture(scope="class")
def app():
    _app = create_app(test_config={"TESTING": True,
                                   "DATABASE": "postgresql://pepel:123@localhost/collegue",
                                   "SERVER_NAME": "test_api"})
    api = Api(_app)
    db = SQLAlchemy(_app)
    add_urls(api)
    yield _app


@pytest.fixture(scope="function")
def client(app):
    # client = app.test_client()
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope="function")
def session():
    engine = create_engine("postgresql://pepel:123@localhost/collegue")
    session = Session(engine)
    yield session
    session.close()


