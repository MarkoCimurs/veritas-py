from typing import Callable

def settings(runs: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        func.runs = runs
        return func
    return decorator
