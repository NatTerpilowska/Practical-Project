from flask import url_for
from flask_testing import TestCase

from service_3.app import app, clas

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_clas(self):
        for _ in range(20):
            response = self.client.get(url_for('get_clas'))

            self.assert200(response)
            self.assertIn(response.data.decode(), clas)
        