"""
Creates an HDF5 file with a single dataset of shape (channels, n),
filled with random numbers.

Writing to the different channels (rows) is parallelized using MPI.

Usage:
  mpirun -np 8 python demo.py

Small shell script to run timings with different numbers of MPI processes:

  for np in 1 2 4 8 12 16 20 24 28 32; do
      echo -n "$np ";
      /usr/bin/time --format="%e" mpirun -np $np python demo.py;
  done

"""

from mpi4py import MPI
import h5py
import numpy as np


n = 100000000
channels = 32
num_processes = MPI.COMM_WORLD.size
rank = MPI.COMM_WORLD.rank  # The process ID (integer 0-3 for 4-process run)

np.random.seed(746574366 + rank)

f = h5py.File('parallel_test.hdf5', 'w', driver='mpio', comm=MPI.COMM_WORLD)
dset = f.create_dataset('test', (channels, n), dtype='f')

for i in range(channels):
    if i % num_processes == rank:
       #print("rank = {}, i = {}".format(rank, i))
       data = np.random.uniform(size=n)
       dset[i] = data

f.close()

"""
Some example timings on my workstation (32 cores):

1	61.98	70.05	64.61	63.47
2	33.22	33.53	34.85	33.45
4	44.6	20.38	20.3	19
8	13.3	13.76	14.5	13.55
12	14.62	14.98	12.75	33.24
16	12	13.19	14.76	13.68
20	14.75	14.82	14.46	14.33
24	16.69	15.81	16.94	15.98
28	17.61	18	17.56	17.78
32	35.31	35.7	16.16	39.88

"""