from game_object import GameObject

class Building(GameObject):
    def __init__(self, object_id: int, name: str, x: int, y: int,
                 built: bool = False):
        super().__init__(object_id, name, x, y)
        self._built = built

    def isBuilt(self) -> bool:
        return self._built

    def build(self) -> None:
        self._built = True