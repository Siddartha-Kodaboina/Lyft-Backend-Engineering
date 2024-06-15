import unittest
from datetime import datetime, timedelta
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class TestCar(unittest.TestCase):
    def test_car_needs_service_due_to_capulet_engine(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=30001)
        battery = SpindlerBattery(last_service_date=datetime.today().date(), current_date=datetime.today().date())
        car = Car([engine, battery])
        self.assertTrue(car.needs_service())

    def test_car_needs_service_due_to_sternman_engine(self):
        engine = SternmanEngine(warning_light_on=True)
        battery = SpindlerBattery(last_service_date=datetime.today().date(), current_date=datetime.today().date())
        car = Car([engine, battery])
        self.assertTrue(car.needs_service())

    def test_car_needs_service_due_to_willoughby_engine(self):
        engine = WilloughbyEngine(last_service_mileage=0, current_mileage=60001)
        battery = SpindlerBattery(last_service_date=datetime.today().date(), current_date=datetime.today().date())
        car = Car([engine, battery])
        self.assertTrue(car.needs_service())

    def test_car_needs_service_due_to_spindler_battery(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=1000)
        last_service_date = datetime.today().date() - timedelta(days=365 * 3)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=datetime.today().date())
        car = Car([engine, battery])
        self.assertTrue(car.needs_service())

    def test_car_needs_service_due_to_nubbin_battery(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=1000)
        last_service_date = datetime.today().date() - timedelta(days=365 * 5)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=datetime.today().date())
        car = Car([engine, battery])
        self.assertTrue(car.needs_service())

    def test_car_does_not_need_service(self):
        engine = CapuletEngine(last_service_mileage=0, current_mileage=1000)
        battery = SpindlerBattery(last_service_date=datetime.today().date(), current_date=datetime.today().date())
        car = Car([engine, battery])
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
