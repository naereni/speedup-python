### main file of vanila python

import cProfile
import random


# fibonacci number with index n
def fib(n: int):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)


# list of Prime numbers up to a number n
def list_prime_num(n: int):
    # check 
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


# factorial
def fac(n: int):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p


# auxiliary function for sorting algorithm
def array_nums(length: int):
    raw_nums = []
    for i in range(1, length):
        raw_nums.append(random.randint(0, 1000000))
    return raw_nums


# yes yes the most stupid version of bubble sort
def bubble_sort(nums: list):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums