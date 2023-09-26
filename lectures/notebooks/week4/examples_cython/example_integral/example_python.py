import numpy as np

def f(x):
    return x**2-x

def integrate_f_py(a, b, N):
    s = 0
    dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx) + f(a+(i+1)*dx)
    return s * dx * 0.5

def integrate_f_np(a, b, N):
    dx = (b-a)/N
    x_arr = np.linspace(a, b, N+1)
    y_arr = f(x_arr)
    s_arr = (y_arr[1:] + y_arr[:-1])*dx*0.5
    return np.sum(s_arr)
