class GameObject:
    def __init__(self, object_id: int, name: str, x: int, y: int):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def getID(self) -> int:
        return self._id

    def getName(self) -> str:
        return self._name

    def getX(self) -> int:
        return self._x

    def getY(self) -> int:
        return self._y