from serviceable import Serviceable

class OctoprimeTires(Serviceable):
    def __init__(self, tire_wear: list[float]):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3
