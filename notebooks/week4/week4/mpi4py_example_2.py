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

    comm.Bcast([y_arr, MPI.DOUBLE], root=0)
    comm.Bcast([x_arr, MPI.DOUBLE], root=0)

    if rank == 0:
        sendbuf = np.arange(N_arr)
        ave, res = divmod(len(sendbuf), size)
        count = [ave + 1 if p < res else ave for p in range(size)]
        count = np.array(count)
        displ = [sum(count[:p]) for p in range(size)]
        displ = np.array(displ)
    else:
        sendbuf = None
        count = np.zeros(size, dtype=int)
        displ = np.zeros(size, dtype=int)
    comm.Bcast(count, root=0)
    comm.Bcast(displ, root=0)
    recvbuf = np.zeros(count[rank])
    comm.Scatterv([sendbuf, count, displ, MPI.DOUBLE], recvbuf, root=0)

    S_loc = np.array([0.0])
    comm.Bcast([S_loc, MPI.DOUBLE], root=0)
    i_s = displ[rank]
    i_e = displ[rank]+count[rank]
    S_loc[0] = simpson_local_arr(y_arr, x_arr, i_s, i_e)
    comm.Barrier()

    if rank==0:
        S_tot = np.array([0.0])
    else:
        S_tot = None

    comm.Reduce(
        [S_loc, MPI.DOUBLE],
        [S_tot, MPI.DOUBLE],
        op=MPI.SUM,
        root=0)

    if rank==0:
        print("S = ", S_tot)
