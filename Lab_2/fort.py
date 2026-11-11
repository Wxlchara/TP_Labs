from building import Building
from attacker import Attacker
from unit import Unit

class Fort(Building, Attacker):
    def __init__(self, object_id: int, name: str, x: int, y: int,
                 damage: float, built: bool = False):
        super().__init__(object_id, name, x, y, built)
        self._damage = max(0.0, damage)

    def attack(self, unit: Unit) -> None:
        if self.isBuilt() and unit.isAlive():
            unit.receiveDamage(self._damage)  