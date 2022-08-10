# Astract class methods

from abc import ABC, abstractmethod

class car(ABC):
    @abstractmethod
    def test_driver(self):
        pass

class BMW(car):

    def test_driver(self,color):
        print(f'"driver of {color} BMW Car"')


# c = car()
bmw = BMW()
bmw.test_driver('green')