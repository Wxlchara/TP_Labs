from abc import ABC, abstractmethod

class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def setDough(self, dough):
        self.dough = dough

    def setSauce(self, sauce):
        self.sauce = sauce

    def setTopping(self, topping):
        self.topping = topping

    def __str__(self):
        return f"Pizza: {self.dough}, {self.sauce}, {self.topping}"

class PizzaBuilder(ABC):
    @abstractmethod
    def buildDough(self):
        pass

    @abstractmethod
    def buildSauce(self):
        pass

    @abstractmethod
    def buildTopping(self):
        pass

    @abstractmethod
    def getResult(self):
        pass

class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def buildDough(self):
        self.pizza.setDough("cross")

    def buildSauce(self):
        self.pizza.setSauce("mild")

    def buildTopping(self):
        self.pizza.setTopping("ham+pineapple")

    def getResult(self):
        return self.pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def constructPizza(self):
        self.builder.buildDough()
        self.builder.buildSauce()
        self.builder.buildTopping()

if __name__ == "__main__":
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)

    director.constructPizza()
    pizza = builder.getResult()

    print(pizza)