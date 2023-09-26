cdef f(double x):
    return x**2-x

def integrate_f_cy(double a, double b, int N):
    cdef int i
    cdef double s, x, dx
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx) + f(a+(i+1)*dx)
    return s * dx * 0.5

