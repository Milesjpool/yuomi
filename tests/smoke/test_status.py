import unittest
import time
from multiprocessing import Process
import requests
import main

class TestStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.status_process = Process(target=main, args=(None,))
        cls.status_process.start()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.status_process.terminate()

    def test_status_code_is_ok(self):
        url = 'http://localhost:8081/status'
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
