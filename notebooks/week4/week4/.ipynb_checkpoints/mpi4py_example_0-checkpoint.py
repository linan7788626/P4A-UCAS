def do_something_meaningful():
    return None

from mpi4py import MPI
if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    nruns = 15
    for i in range(rank, nruns, size):
        do_something_meaningful()
        print("Task %d runs on rank %d out of %d cores." % (i, rank, size))
