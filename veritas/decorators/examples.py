from typing import Callable, List, Tuple, Any

class examples:
    def __init__(self, *args) -> None:
        self.examples = args

    def __call__(self, func: Callable) -> Callable:
        func.examples = self.examples
        return func