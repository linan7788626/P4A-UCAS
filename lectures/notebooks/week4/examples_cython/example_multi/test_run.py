import run_python
import run_cython
import time

n = 10000

start = time.time()
run_python.test(n)
end = time.time()

purePython_time = end - start
print ("Pure Python time = {}".format(purePython_time))

start = time.time()
run_cython.test(n)
end = time.time()

Cython_time = end - start
print("Cython time = {}".format(Cython_time))

print("Speedup = {}".format(purePython_time/Cython_time))

