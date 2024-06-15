from serviceable import Serviceable

class CarriganTires(Serviceable):
    def __init__(self, tire_wear: list[float]):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return any(wear >= 0.9 for wear in self.tire_wear)
