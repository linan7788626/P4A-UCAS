from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        [
            'compiled_pure_python_primes.py',
            'cython_primes.pyx',
        ],
    annotate=True
    ),
)
