import unittest

class TestStatus(unittest.TestCase):
    def test_status_code_is_ok(self):
        status_code = 200
        self.assertEqual(status_code, 200)
