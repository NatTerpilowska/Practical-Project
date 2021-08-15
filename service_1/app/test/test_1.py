from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from app import app, db

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_home(self):

        with mock() as m:
            m.get('http://service_2:5000/get/race', text='Human')
            m.get('http://service_3:5000/get/clas', text='Paladin')
            m.post('http://service_4:5000/post/points', json=12)

            response = self.client.get(url_for('home'))

        self.assert200(response)
        