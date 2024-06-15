from car import Car
from engine.model.willoughby_engine import WilloughbyEngine
from engine.model.spindler_battery import SpindlerBattery

class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, last_service_date)
        super().__init__([engine, battery])
