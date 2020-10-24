"""
Implements a sieve of Erasthones.
"""

import numpy as np

def sieve(max_number):

    sieve_array = np.arange(2, max_number+1)
    ind_arr = np.zeros(len(sieve_array))

    index = 0
    max_index = len(sieve_array)

    while index < max_index:
        if ind_arr[index] == 0:
            inner_index = index + sieve_array[index]
            while inner_index < max_index:
                ind_arr[inner_index] = 1
                inner_index += sieve_array[index]
        index += 1

    return np.ma.masked_array(sieve_array, ind_arr).compressed()
