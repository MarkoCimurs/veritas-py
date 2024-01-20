from typing import Callable

class settings:
    def __init__(self, num_runs: int):
        self.num_runs = num_runs

    def __call__(self, test_func: Callable) -> Callable:
        test_func.num_runs = self.num_runs
        return test_func
