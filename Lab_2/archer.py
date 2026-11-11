from unit import Unit
from attacker import Attacker
from moveable import Moveable

class Archer(Unit, Attacker, Moveable):
    def __init__(self, object_id: int, name: str, x: int, y: int,
                 hp: float, damage: float):
        super().__init__(object_id, name, x, y, hp)
        self._damage = max(0.0, damage)

    def attack(self, unit: Unit) -> None:
        if self.isAlive() and unit.isAlive():
            unit.receiveDamage(self._damage)

    def move(self, x: int, y: int) -> None:
        if self.isAlive():
            self._x = x
            self._y = y