import unittest
from datetime import datetime, timedelta
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = datetime.today().date() - timedelta(days=365 * 3)
        battery = SpindlerBattery(last_service_date, datetime.today().date())
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = datetime.today().date() - timedelta(days=365)
        battery = SpindlerBattery(last_service_date, datetime.today().date())
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
