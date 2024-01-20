import os
from .runner import find_tests, run_test_functions

def main():
    for mod in find_tests(os.getcwd()):
        run_test_functions(mod)         

if __name__ == "__main__":
    main()
