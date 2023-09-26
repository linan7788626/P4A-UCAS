# Copyright 2023 cython.org
# This file includes code from https://github.com/cython/cython
# licensed under the Apache License 2.0.

# Description: Python implementation of the primes algorithm

def primes(nb_primes):
    p = []
    n = 2
    while len(p) < nb_primes:
        # Is n prime?
        for i in p:
            if n % i == 0:
                break

        # If no break occurred in the loop
        else:
            p.append(n)
        n += 1
    return p
