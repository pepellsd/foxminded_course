from get_drivers import read_logs_driver_info
from DB import DriverDB, StatisticDB
from peewee import SqliteDatabase


def init_db(database_name="report.db"):
    db = SqliteDatabase(database_name)
    with db:
        db.create_tables([DriverDB, StatisticDB])
    return db


def format_to_db(name_race):
    drivers_arr = read_logs_driver_info()
    lst_drivers = []
    lst_statistic = []
    for index, driver in enumerate(drivers_arr, start=1):
        drv = (driver[0], driver[3])
        lst_drivers.append(drv)
        lst_statistic.append((driver[2], driver[1], name_race, driver[3], index))
    return lst_drivers, lst_statistic


def fill_db(database, data_drivers, data_statistics):
    with database.atomic():
        DriverDB.insert_many(data_drivers,
                             fields=[DriverDB.name, DriverDB.code]).on_conflict("NOTHING").execute()
        StatisticDB.insert_many(data_statistics,
                                fields=[StatisticDB.time, StatisticDB.car,
                                        StatisticDB.title_race,
                                        StatisticDB.driver, StatisticDB.place]).on_conflict("NOTHING").execute()


if __name__ == "__main__":
    database = init_db(database_name="report.db")
    drivers, statistics = format_to_db("monaco_2018")
    fill_db(database=database, data_drivers=drivers, data_statistics=statistics)
