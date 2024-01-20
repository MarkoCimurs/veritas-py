import os
import types
import importlib.util

def find_tests(directory: str) -> list[types.ModuleType]:
    modules = []
    for root, dirs, files in os.walk(directory):
        if 'tests' in dirs:
            test_dir = os.path.join(root, 'tests')
            for file in os.listdir(test_dir):
                if file.startswith('test_') and file.endswith('.py'):
                    file_path = os.path.join(test_dir, file)
                    module_name = os.path.splitext(file)[0]
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    modules.append(module)
    return modules

def run_test_functions(module: types.ModuleType) -> None:
    print(f"module: {module.__name__}")
    for name, obj in vars(module).items():
        if name.startswith('test_') and isinstance(obj, types.FunctionType):
                try:
                    obj()
                    print("\033[92m\tTest {} succeeded\033[0m".format(name))
                except AssertionError:
                    print("\033[91m\tTest {} failed\033[0m".format(name))
