from serviceable import Serviceable
from datetime import date

class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days > 365 * 2
