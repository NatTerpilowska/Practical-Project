from flask import url_for
from flask_testing import TestCase

from service_4.app import app, pointss

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_race(self):

        for race in pointss['race']:
            for clas in pointss['clas']:

                payload = {'race':race, 'clas':clas}
                response = self.client.post(url_for('post_points'), json=payload)

                self.assert200(response)

                expected_points = round((pointss['race'][race] + pointss['clas'][clas]))
                self.assertEqual(response.json, expected_points)