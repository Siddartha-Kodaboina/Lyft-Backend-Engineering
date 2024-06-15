import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.8, 0.7, 0.95]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.7, 0.6, 0.5, 0.4]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
