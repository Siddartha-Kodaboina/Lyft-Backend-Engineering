from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery

class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, last_service_date)
        super().__init__([engine, battery])
