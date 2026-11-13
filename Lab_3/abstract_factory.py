from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("You have created a Windows button.")

class MacButton(Button):
    def paint(self):
        print("You have created a Mac button.")

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("You have created a Windows checkbox.")

class MacCheckbox(Checkbox):
    def paint(self):
        print("You have created a Mac checkbox.")

class GUIFactory(ABC):
    @abstractmethod
    def createButton(self):
        pass

    @abstractmethod
    def createCheckbox(self):
        pass

class WindowsFactory(GUIFactory):
    def createButton(self):
        return WindowsButton()

    def createCheckbox(self):
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def createButton(self):
        return MacButton()

    def createCheckbox(self):
        return MacCheckbox()

class Application:
    def __init__(self, factory):
        self.button = factory.createButton()
        self.checkbox = factory.createCheckbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

if __name__ == "__main__":
    app1 = Application(WindowsFactory())
    app1.paint()

    app2 = Application(MacFactory())
    app2.paint()