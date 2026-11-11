from abc import ABC, abstractmethod

class Moveable(ABC):
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass