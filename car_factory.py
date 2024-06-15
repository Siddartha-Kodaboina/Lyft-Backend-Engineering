from datetime import date
from car import Car
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list[float]) -> Car:
        tires = CarriganTires(tire_wear)
        return Calliope(last_service_date, current_mileage, last_service_mileage, tires)

    @staticmethod
    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list[float]) -> Car:
        tires = OctoprimeTires(tire_wear)
        return Glissade(last_service_date, current_mileage, last_service_mileage, tires)

    @staticmethod
    def create_palindrome(last_service_date: date, warning_light_on: bool, tire_wear: list[float]) -> Car:
        tires = CarriganTires(tire_wear)
        return Palindrome(last_service_date, warning_light_on, tires)

    @staticmethod
    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list[float]) -> Car:
        tires = OctoprimeTires(tire_wear)
        return Rorschach(last_service_date, current_mileage, last_service_mileage, tires)

    @staticmethod
    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list[float]) -> Car:
        tires = CarriganTires(tire_wear)
        return Thovex(last_service_date, current_mileage, last_service_mileage, tires)
