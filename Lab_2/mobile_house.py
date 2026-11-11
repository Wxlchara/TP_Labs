from building import Building
from moveable import Moveable

class MobileHouse(Building, Moveable):
    def move(self, x: int, y: int) -> None:
        if self.isBuilt():
            self._x = x
            self._y = y