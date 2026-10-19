
from abc import ABC, abstractmethod

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

b = Bank(5000)
print("Balance:", b.get_balance())

s = Square(4)
print("Area of Square:", s.area())
s