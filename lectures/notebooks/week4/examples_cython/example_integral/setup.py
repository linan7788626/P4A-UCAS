from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "example_cython",
        ["example_cython.pyx"],
    ),
]

setup(
    name="example_cython",
    ext_modules=cythonize(ext_modules,
                          annotate=True
                          ),
)
