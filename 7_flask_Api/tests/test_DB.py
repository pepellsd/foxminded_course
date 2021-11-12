import pytest

from DB import DriverDB, StatisticDB


@pytest.mark.usefixtures('db')
class TestDB:
    def test_len_records(self):
        assert len(DriverDB.select()) == 19
        assert len(StatisticDB.select()) == 19

    def test_execute(self, cursor):
        cursor.execute("INSERT INTO drivers VALUES(?,?)", ("name", "code"))
        assert len(DriverDB.select()) == 20

    def test_correct_data(self):
        first = DriverDB.select()[0]
        last = DriverDB.select()[18]
        assert first.name == "Lewis Hamilton"
        assert last.name == "Kevin Magnussen"

    def test_get_driver_by_code(self):
        driver = DriverDB.select().where(DriverDB.code == "SPF")[0]
        assert driver.code == "SPF"
        assert driver.name == "Sergio Perez"

    def test_get_stat(self):
        driver = DriverDB.select(DriverDB, StatisticDB).join(StatisticDB, attr='stat').where(
                                                             StatisticDB.car == "FERRARI")[0]
        assert driver.stat.car == "FERRARI"
        assert driver.stat.title_race == "monaco_2018"