gcc -O2 --shared example.c -o example.so
cython example_cython.pyx
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I `python -c "import distutils.sysconfig;print(distutils.sysconfig.get_python_inc())"` -o example_cython.so example_cython.c example.so
LD_LIBRARY_PATH="." python demo.py
