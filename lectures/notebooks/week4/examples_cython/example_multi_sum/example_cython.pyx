cdef extern from "example.h":
    int multi_sum_c(int)

def multi_sum(int a):
    return multi_sum_c(a)
