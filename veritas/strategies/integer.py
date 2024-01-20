import random
from .strategy import Strategy

class Integer(Strategy):
    def __init__(self, min_value: int =-100, max_value: int =100) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def generate(self) -> int:
        return random.randint(self.min_value, self.max_value)

