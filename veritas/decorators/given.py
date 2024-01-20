from functools import wraps
from ..strategies import Strategy
from typing import Any, Callable

def given(*strategy_instances: Strategy) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            generated = [strategy.generate() for strategy in strategy_instances]
            return func(*generated, *args, **kwargs)
        return wrapper
    return decorator