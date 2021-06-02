from unittest import TestCase
import requests


class EmailTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = requests.Session()
        cls._url = 'http://localhost:8000/api/v1/email/'

    def test_email_valid(self):
        data = {
            "email": "at8029@srmist.edu.in",
            "name": "Aradhya"
        }
        response = self.request.post(self._url, data=data)
        self.assertEqual(response.status_code, 201)

    def test_email_invalid(self):
        data = {
            "email": "testemail",
            "name": "someone"
        }
        response = self.request.post(self._url, data=data)
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        pass
