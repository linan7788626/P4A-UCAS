from example_python import integrate_f_py
from example_python import integrate_f_np
from example_cython import integrate_f_cy
import time

if __name__ == '__main__':
    a_in = 1.0
    b_in = 10.0
    nbins = 2000000

    print ("============")
    start = time.time()
    print ("Pure Python Results = {}".format(integrate_f_py(a_in, b_in, nbins)))
    end = time.time()
    purePython_time = end - start
    print ("Pure Python TIME = {}".format(purePython_time))
    print ("============")
    start = time.time()
    print ("Python Numpy RESULTS = {}".format(integrate_f_np(a_in, b_in, nbins)))
    end = time.time()
    pythonNumpy_time = end - start
    print ("Python Numpy TIME = {}".format(pythonNumpy_time))
    print ("============")
    start = time.time()
    print ("Cython RESULTS = {}".format(integrate_f_cy(a_in, b_in, nbins)))
    end = time.time()
    cython_time = end - start
    print ("Cython TIME = {}".format(cython_time))
