import unittest
from fastapi.testclient import TestClient
from main import app

class TestFastAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_convert_valid_string_to_int(self):
        response = self.client.get("/convert/1234")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 1234)

    def test_convert_invalid_string_to_int(self):
        response = self.client.get("/convert/abc")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), None)

    def test_convert_string_with_commas_to_int(self):
        response = self.client.get("/convert/12,345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 12345)

    def test_convert_string_with_currency_symbol_to_int(self):
        response = self.client.get("/convert/USD12345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 12345)

    def test_convert_string_with_non_integer_characters(self):
        response = self.client.get("/convert/total score: 44")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 44)

    def test_convert_string_with_all_non_integer_characters(self):
        response = self.client.get("/convert/bought 2 burgers for 33 bucks")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 233)

if __name__ == "__main__":
    unittest.main()