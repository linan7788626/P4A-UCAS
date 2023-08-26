import numpy as np
from multiprocessing import Pool

def simpson_tmp_arr(data_pairs):
    y = data_pairs[0]
    x = data_pairs[1]
    N = int(len(y))
    dx = x[1] - x[0]
    S = 0
    for i in range(1, N, 2):
        S += dx/3 * (y[i-1] + 4.0*y[i] + y[i+1])
    return S

if __name__ == '__main__':
    N_arr = 100000004; # how to define this number properly?
    a_arr = 0.0;
    b_arr = np.pi/2;
    x_arr = np.linspace(a_arr, b_arr, N_arr)
    y_arr = np.sin(x_arr)

    cores = 4

    y_parts = np.array_split(y_arr, cores)
    x_parts = np.array_split(x_arr, cores)

    pairs_parts = [[y_i, x_i] for [y_i, x_i] in zip(y_parts, x_parts)]

    with Pool(cores) as p:
        parts = p.map(simpson_tmp_arr, pairs_parts)

    print("Result = %.20f"%(np.sum(parts)))
