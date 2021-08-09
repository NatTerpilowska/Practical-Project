from flask import url_for
from flask_testing import TestCase

from service4.app import app, points

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_race(self):

        for race in points['race']:
            for class in points['class']:

                payload = {'race':race, 'class':class}
                response = self.client.post(url_for('post_order'), json=payload)

                self.assert200(response)

                expected_points = round((points['race'][race] + points['class'][class]))
                self.assertEqual(response.json, expected_points)