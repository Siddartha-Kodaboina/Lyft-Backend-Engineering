from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self, components: list[Serviceable]):
        self.components = components

    def needs_service(self) -> bool:
        return any(component.needs_service() for component in self.components)
