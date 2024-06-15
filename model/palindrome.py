from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, last_service_date)
        super().__init__([engine, battery])
