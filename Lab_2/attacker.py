from abc import ABC, abstractmethod
from unit import Unit

class Attacker(ABC):
    @abstractmethod
    def attack(self, unit: Unit) -> None:
        pass