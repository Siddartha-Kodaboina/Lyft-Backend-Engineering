from datetime import date
from car import Car
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarFactory:
    @staticmethod
    def create_calliope(last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Calliope(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Glissade(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(last_service_date: date, warning_light_on: bool) -> Car:
        return Palindrome(last_service_date, warning_light_on)

    @staticmethod
    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Rorschach(last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Thovex(last_service_date, current_mileage, last_service_mileage)