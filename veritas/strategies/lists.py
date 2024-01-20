import random
from .strategy import Strategy

class Lists:
    def __init__(self, strategy: Strategy, min_length: int = 1, max_length: int = 10) -> None:
        self.strategy = strategy
        self.min_length = min_length
        self.max_length = max_length

    def generate(self) -> list:
        length = random.randint(self.min_length, self.max_length)
        return [self.strategy.generate() for _ in range(length)]