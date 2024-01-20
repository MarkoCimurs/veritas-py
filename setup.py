from setuptools import setup, find_packages

setup(
    name='veritas',
    version='0.1',
    packages=find_packages(),
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'veritas = veritas.main:main'
        ]
    },
)