from setuptools import setup, Extension
import Cython
from Cython.Build import cythonize


# setup(
    # name='example_cython',
    # ext_modules = cythonize("example_cython.pyx")
# )

extensions = [
    Extension("example_cython",
              sources=["example_cython.pyx"],
              include_dirs=["./"],
              libraries=["m"],
              library_dirs=["./"]),
]
setup(
    name='example_cython',
    ext_modules=cythonize(extensions),
)

# Cython.Build.cythonize(module_list, exclude=None, nthreads=0, aliases=None, quiet=False, force=None, language=None, exclude_failures=False, show_all_warnings=False, **options)
# extensions = [
    # Extension("primes", ["primes.pyx"],
        # include_dirs=[...],
        # libraries=[...],
        # library_dirs=[...]),
    # # Everything but primes.pyx is included here.
    # Extension("*", ["*.pyx"],
        # include_dirs=[...],
        # libraries=[...],
        # library_dirs=[...]),
# ]
# setup(
    # name="My hello app",
    # ext_modules=cythonize(extensions),
# )

#####
#
# from setuptools import setup, find_packages
#
# setup(
#     name='example',
#     version='0.1.0',
#     description='Setting up a python package',
#     author='Rogier van der Geer',
#     author_email='rogiervandergeer@godatadriven.com',
#     url='https://blog.godatadriven.com/setup-py',
#     packages=find_packages(include=['exampleproject', 'exampleproject.*']),
#     install_requires=[
#         'PyYAML',
#         'pandas==0.23.3',
#         'numpy>=1.14.5'
#     ],
#     extras_require={'plotting': ['matplotlib>=2.2.0', 'jupyter']},
#     setup_requires=['pytest-runner', 'flake8'],
#     tests_require=['pytest'],
#     entry_points={
#         'console_scripts': ['my-command=exampleproject.example:main']
#     },
#     package_data={'exampleproject': ['data/schema.json']}
#     )
