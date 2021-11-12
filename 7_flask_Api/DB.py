from peewee import *

db = SqliteDatabase("report.db")


class DriverDB(Model):
    name = CharField()
    code = CharField(primary_key=True)

    class Meta:
        database = db
        table_name = "drivers"


class StatisticDB(Model):
    id = AutoField()
    time = DateTimeField(index=True)
    car = CharField()
    title_race = CharField()
    place = IntegerField()
    driver = ForeignKeyField(DriverDB, backref="stats", index=True, on_delete='CASCADE')

    class Meta:
        database = db
        table_name = "drivers_stat"
        indexes = (
            (('title_race', 'driver'), True),
        )



def race_stats_query(race="monaco_2018"):
    return (
        StatisticDB.select(StatisticDB, DriverDB)
        .join(DriverDB)
        .where(StatisticDB.title_race == race)
        .order_by(StatisticDB.time)
    )

