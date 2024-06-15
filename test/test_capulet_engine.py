import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=30001)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=30000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
