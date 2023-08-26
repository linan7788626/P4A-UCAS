import numpy as np
from multiprocessing import Pool

def mc_and_count_points_part(n):
    count = 0
    for i in range(int(n)):
        x=np.random.random()
        y=np.random.random()
        if x*x + y*y <= 1:
            count=count+1
    return count

if __name__ == '__main__':
    cores = multiprocessing.cpu_count()
    print('You have {0:1d} CPUs'.format(cores))
    cores = 8
    n = 10000000
    part_count=[n/cores for i in range(cores)] # not accurate
    with Pool(cores) as p:
        count=p.map(monte_carlo_pi_part, part_count)

    print("Esitmated value of Pi:: ", sum(count)/(n*1.0)*4  )
