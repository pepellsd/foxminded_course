from flask import Flask, request, abort, jsonify, make_response
from flasgger import Swagger, Schema, SwaggerView, fields
import simplexml

from config import Config_app
from DB import race_stats_query, DriverDB, StatisticDB


def create_app(test_config=None):
    application = Flask(__name__)
    application.config.from_object(Config_app)
    if test_config:
        application.config.update(test_config)
    return application


app = create_app()
swagger = Swagger(app)
api_ver = "v1"


class Driver(Schema):
    car = fields.Str()
    code = fields.Str()
    name = fields.Str()
    place = fields.Int()
    time = fields.Str()


class NamesCodes(Schema):
    name = fields.Str()
    code = fields.Str()


class DriversView(SwaggerView):
    responses = {
        200: {
            "description": "common statistic drivers",
            "schema": Driver,
        }
    }

    def get(self):
        drivers = []
        for stat in race_stats_query():
            res = dict(
                name=stat.driver.name,
                car=stat.car,
                time=stat.time,
                code=stat.driver.code,
                place=stat.place
            )
            drivers.append(res)
        if request.args.get("format") == "xml":
            xml_drivers = simplexml.dumps({"drivers": drivers})
            return make_response(xml_drivers, 200)
        return jsonify(drivers)


class NamesCodesView(SwaggerView):
    responses = {
        200: {
            "description": "names and codes of drivers",
            "schema": NamesCodes
        }
    }

    def get(self):
        query_names_codes = DriverDB.select()
        names_codes = [dict(name=driver.name, code=driver.code) for driver in query_names_codes]
        if request.args.get("format") == "xml":
            xml_names_codes = simplexml.dumps({"names_codes": names_codes})
            return make_response(xml_names_codes, 200)
        return jsonify(names_codes)


class DriverView(SwaggerView):
    parameters = [
        {
            "name": "code",
            "in": "path",
            "type": "string",
            "required": True,
            "default": "LHM",
            "limit": 1
        }
    ]
    responses = {
        200: {
            "description": "statistic about driver",
            "schema": Driver
        }
    }

    def get(self, code):
        query_driver = DriverDB.select(DriverDB, StatisticDB).join(StatisticDB, attr='stat').where(
            DriverDB.code == code).first()
        if not query_driver:
            abort(404)
        driver = dict(car=query_driver.stat.car, code=query_driver.code, name=query_driver.name,
                      place=query_driver.stat.place, time=query_driver.stat.time)
        if request.args.get("format") == "xml":
            xml_names_codes = simplexml.dumps({"driver": driver})
            return make_response(xml_names_codes, 200)
        return jsonify(driver)


@app.errorhandler(404)
def err_404(error):
    return error


def add_urls_rules(app):
    app.add_url_rule(f"/api/{api_ver}/report/drivers",
                     view_func=DriversView.as_view("Drivers"), methods=['GET'])
    app.add_url_rule(f"/api/{api_ver}/report/names_codes",
                     view_func=NamesCodesView.as_view("NamesCodes"), methods=['GET'])
    app.add_url_rule(f"/api/{api_ver}/report/driver/<string:code>",
                     view_func=DriverView.as_view("Driver"), methods=['GET'])


add_urls_rules(app)

if __name__ == '__main__':
    app.run()
