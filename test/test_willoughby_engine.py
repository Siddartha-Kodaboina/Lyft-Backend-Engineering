import unittest
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(last_service_mileage=0, current_mileage=60001)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(last_service_mileage=0, current_mileage=60000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
