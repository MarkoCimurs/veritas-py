from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def generate(self):
        pass