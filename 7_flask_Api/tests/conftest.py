import pytest
from peewee import SqliteDatabase

from init_fill_db import fill_db, format_to_db
from DB import DriverDB, StatisticDB
from api import create_app, add_urls_rules


@pytest.fixture(scope="class")
def db():
    db = SqliteDatabase(":memory:")
    StatisticDB.bind(db)
    DriverDB.bind(db)
    db.create_tables([DriverDB, StatisticDB])
    drivers, statistics = format_to_db(name_race="monaco_2018")
    fill_db(database=db, data_drivers=drivers, data_statistics=statistics)
    yield db
    db.drop_tables([DriverDB, StatisticDB])
    db.close()


@pytest.fixture(scope="function")
def cursor(db):
    cursor = db.cursor()
    yield cursor
    cursor.close()


@pytest.fixture()
def client(db):
    app = create_app({"TESTING": True, "DATABASE": db, "SERVER_NAME": "test"})
    add_urls_rules(app)
    with app.test_client() as client:
        with app.app_context():
            yield client