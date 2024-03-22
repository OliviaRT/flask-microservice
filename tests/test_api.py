import unittest
import json

from app import app
app.testing = True


class TestApi(unittest.TestCase):

    def test_caculate(self):
        with app.test_client() as client:
            data = {'salary': 2000, 'expenses': 1000}
            result = client.post('/calculate', data=data)
            self.assertEqual(result.data, json.dumps(data))
