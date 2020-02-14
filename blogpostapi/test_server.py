import requests
import unittest
import json

# import web

BASE_URL = 'http://127.0.0.1:8080/'
FETCH_URL = BASE_URL + 'posts'
POST_URL = BASE_URL + 'post'


class TestWebApi(unittest.TestCase):

    # def setUp(self):
    def test_wrong_url(self):
        resp = requests.get(BASE_URL)
        self.assertEqual(resp.status_code, 404)

    def test_get_all(self):
        resp = requests.get(FETCH_URL)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(len(resp.json()), 1)

        self.assertEqual(resp.json(), [{"post_id": 1, "title": "hai", "body": "hai"}])

    def test_post(self):
        resp = requests.post(POST_URL, data={'title': 'number 2', 'body': 'number 2'})
        resp = requests.get(FETCH_URL)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(len(resp.json()), 2)

        self.assertEqual(resp.json(),
                         [{'post_id': 1, 'title': 'hai', 'body': 'hai'}, {'title': 'number 2', 'body': 'number 2'}])

    # def test_db(self):


if __name__ == "__main__":
    unittest.main()
