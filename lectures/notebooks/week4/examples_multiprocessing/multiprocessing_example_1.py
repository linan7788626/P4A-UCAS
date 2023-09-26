import numpy as np
from multiprocessing import Pool, cpu_count

def monte_carlo_pi_part(n):
    count = 0
    for i in range(int(n)):
        x=np.random.random()
        y=np.random.random()
        if x*x + y*y <= 1:
            count=count+1
    return count

if __name__ == '__main__':
    cores = 4
    print('You have %d CPUs, and you use %d cores for the calculation'%(cpu_count(), cores))
    n = 10000000
    part_count=[n/cores for i in range(cores)] # not accurate, can you improve it?
    with Pool(cores) as p:
        count=p.map(monte_carlo_pi_part, part_count)

    print("Esitmated value of Pi:: ", sum(count)/(n*1.0)*4  )
