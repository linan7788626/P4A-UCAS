cdef extern from "example.h":
    int mult_sum_c(int)

def mult_sum(int a):
    return mult_sum_c(a)
