from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def move(self):
        """
        move abstract method
        """
        pass