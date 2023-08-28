import numpy as np

def simpson_local_arr(y, x, i_start, i_end):
    dx = x[1] - x[0]
    S = 0
    if i_end >= len(x):
        i_end = int(len(x))
    for i in range(i_start, i_end, 2):
        S += dx/3 * (y[i-1] + 4.0*y[i] + y[i+1])
    return S

from mpi4py import MPI
if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    dest=0
    total=-1.0

    N_arr = 100000001; # is this number even or odd?
    a_arr = 0.0;
    b_arr = np.pi/2;
    x_arr = np.linspace(a_arr, b_arr, N_arr)
    y_arr = np.sin(x_arr)

    local_n = int(N_arr/size)
    i_s = 1+rank*local_n
    i_e = i_s + local_n

    integral = simpson_local_arr(y_arr, x_arr, i_s, i_e)

    if rank == 0:
        total = integral
        for source in range(1,size):
            integral = comm.recv(source=source)
            print("PE ", rank, "<-", source, ",", integral, "\n")
            total = total + integral
    else:
        print("PE ", rank, "->", dest, ",", integral, "\n")
        comm.send(integral, dest=0)

    if (rank == 0):
        print("\n")
        print("With n = ", N_arr, "bins, \n")
        print("integral of sine(x) from", a_arr, "to", b_arr, "=", total, "\n")
    MPI.Finalize
