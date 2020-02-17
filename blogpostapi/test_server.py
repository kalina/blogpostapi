import itertools
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

    def ordered(self, obj):
        if isinstance(obj, dict):
            return sorted((k, obj.ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(obj.ordered(x) for x in obj)
        else:
            return obj

    def test_post(self):
        expected_out = [{"post_id": 1, "title": "hai", "body": "hai"}, {"title": "number 2", "body": "number 2"}]
        resp = requests.post(POST_URL, json={'title': 'number 2', 'body': 'number 2'})
        self.assertEqual(resp.status_code, 201)
        resp = requests.get(FETCH_URL)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(len(resp.json()), 2)
        #self.assertEqual(self.ordered(expected_out), self.ordered(json.loads(resp.json)))
        #dump = json.dumps(dict_, sort_keys=True, indent=2)
        #self.assertCountEqual(expected_out.items, resp.json().items)
        #set_1 = set(tuple(sorted d.items())) for d in expected_out)
        #set_2 = set(tuple(sorted d.items())) for d in resp.json)
        pairs = zip(expected_out, resp.json())
        self.assertTrue(any(x != y for x, y in pairs))


if __name__ == "__main__":
    unittest.main()
