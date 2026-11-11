from game_object import GameObject

class Unit(GameObject):
    def __init__(self, object_id: int, name: str, x: int, y: int, hp: float):
        super().__init__(object_id, name, x, y)
        self._hp = max(0.0, hp)

    def isAlive(self) -> bool:
        return self._hp > 0

    def getHp(self) -> float:
        return self._hp

    def receiveDamage(self, damage: float) -> None:
        if damage < 0:
            raise ValueError("Damage cannot be negative")

        self._hp = max(0.0, self._hp - damage)  