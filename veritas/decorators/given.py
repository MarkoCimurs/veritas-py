from functools import wraps
from ..strategies import Strategy
from typing import Any, Callable


class given:
    def __init__(self, *strategies: Strategy):
        self.strategies = strategies

    def __call__(self, test_func: Callable) -> Callable:
        def wrapped_test(*args, **kwargs):

            examples = getattr(test_func, 'examples', None)
            if examples is not None:
                for example in examples:
                    test_func(*example, *args, **kwargs)
                        
            num_runs = getattr(test_func, 'num_runs', 50)
            for _ in range(num_runs): 
                test_inputs = [strategy.generate() for strategy in self.strategies]  
                test_func(*test_inputs, *args, **kwargs)
            
        return wrapped_test