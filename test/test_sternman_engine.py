import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = SternmanEngine(warning_light_on=True)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
