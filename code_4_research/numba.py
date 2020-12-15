### main file of vanila python

'''
i dont use cProfiler becouse Numba call
too many func (i dont known how many)
(ಠ_ಠ)
'''

import timeit

fibonacci = '''
from numba import njit

@njit
def fib(n: int):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

fib(40)
'''


list_prime_num = '''
from numba import njit
# list of Prime numbers up to a number n
@njit
def list_prime_num(n: int):
    def is_prime(n: int):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    res_list = []
    for num in range(1, n):
        if is_prime(num):
            res_list.append(num)
    return res_list

list_prime_num(5000)
'''


factorial = '''
from numba import njit
@njit
def fac(n: int):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

fac(100000)
'''


bubble_sort = '''
import random
from numba import njit
# auxiliary function for sorting algorithm
@njit
def array_nums(length: int):
    raw_nums = []
    for i in range(1, length):
        raw_nums.append(random.randint(0, 1000000))
    return raw_nums


# yes yes yes the most stupid version of bubble sort
@njit
def bubble_sort(nums: list):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

bubble_sort(array_nums(10000))
'''


timeit.timeit(fibonacci)
timeit.timeit(list_prime_num)
timeit.timeit(factorial)
timeit.timeit(bubble_sort)