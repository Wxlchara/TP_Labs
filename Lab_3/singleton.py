class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def getInstance():
        return Singleton()

    def someMethod(self):
        print("Singleton is working")

if __name__ == "__main__":
    first = Singleton.getInstance()
    second = Singleton.getInstance()

    print("Same instance:", first is second)
    first.someMethod()