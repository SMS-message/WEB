import unittest
import requests
import datetime as dt

class MyTestCase(unittest.TestCase):
    def test_all_jobs(self):
        self.assertEqual({'jobs': [
            {'job': 'deployment of residential modules 1 and 2', 'start_date': '2025-03-11 14:34:04', 'team_leader': 1,
             'work_size': 15}]},
                          requests.get("http://127.0.0.1:8080/api/jobs").json())

    def test_one_job(self):
        self.assertEqual({'job': {'job': 'deployment of residential modules 1 and 2', 'start_date': '2025-03-11 14:34:04', 'team_leader': 1, 'work_size': 15}}, requests.get("http://127.0.0.1:8080/api/jobs/1").json())

    def test_incorrect_job(self):
        self.assertEqual({'error': 'Not found'}, requests.get("http://127.0.0.1:8080/api/jobs/159").json())

    def test_string_job(self):
        self.assertEqual({'error': 'Not found'}, requests.get("http://127.0.0.1:8080/api/jobs/string").json())

    def test_correct_post(self):
        test_date = dt.date(2020, 11, 7)
        data = {
            "team_leader": 1,
            "job": "testing_systems",
            "work_size": 10,
            "collaborators": "3, 4",
            "start_date": test_date.strftime("%Y-%m-%d %H:%M:%S"),
            "is_finished": False
        }

        self.assertEqual(requests.post("http://127.0.0.1:8080/api/jobs", json=data).json(), {"status": "OK"})

    def test_empty_post(self):
        data = {}
        self.assertEqual(requests.post("http://127.0.0.1:8080/api/jobs", json=data).json(), {"error": "Empty request"})

    def test_incorrect_post(self):
        test_date = dt.date(2020, 11, 7)

        data = {
            "team_leader": "1",
            "job": "testing_systems",
            "collaborators": "3, 4",
            "start_date": test_date.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.assertEqual(requests.post("http://127.0.0.1:8080/api/jobs", json=data).json(), {'error': 'Bad request'})

if __name__ == '__main__':
    unittest.main()
