from flask import url_for


class TestApi:
    def test_drivers_json(self, client):
        response = client.get(url_for("Drivers"))
        drivers = response.get_json()
        assert bytes("LHM", encoding="utf8") in response.data if len(drivers) else False
        assert response.mimetype == "application/json"
        assert bytes("VBM", encoding="utf8") in response.data

    def test_drivers_xml(self, client):
        response = client.get(url_for("Drivers", format="xml"))
        assert bytes("VBM", encoding="utf8") in response.data if len(response.data) else False
        assert response.mimetype == "text/html"
        assert "xml" in response.get_data(as_text=True)
        assert bytes("LHM", encoding="utf8") in response.data

    def test_names_codes_json(self, client):
        response = client.get(url_for("NamesCodes"))
        names_codes = response.get_json()
        assert bytes("Brendon Hartley", encoding="utf8") in response.data if len(names_codes) else False
        assert response.mimetype == "application/json"
        assert bytes("RGH", encoding="utf8") in response.data


    def test_names_codes_xml(self, client):
        response = client.get(url_for("NamesCodes", format="xml"))
        assert bytes("Brendon Hartley", encoding="utf8") in response.data if len(response.data) else False
        assert response.mimetype == "text/html"
        assert "xml" in response.get_data(as_text=True)
        assert bytes("RGH", encoding="utf8") in response.data

    def test_1driver_json(self, client):
        response = client.get(url_for("Driver", code="SPF"))
        driver = response.get_json()
        assert bytes("SPF", encoding="utf8") in response.data if len(driver) else False
        assert response.mimetype, "application/json"
        assert bytes("Sergio Perez", encoding="utf8") in response.data

    def test_1driver_xml(self, client):
        response = client.get(url_for("Driver", code="SPF", format="xml"))
        assert bytes("SPF", encoding="utf8") in response.data if len(response.data) else False
        assert response.mimetype == "text/html"
        assert "xml" in response.get_data(as_text=True)

    def test_invalid_code_driver(self, client):
        response = client.get(url_for("Driver", code="dkfjk"), follow_redirects=True)
        assert response.status_code == 404