from serviceable import Serviceable

class SternmanEngine(Serviceable):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
