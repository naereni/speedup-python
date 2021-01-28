### main file of vanila python

import cProfile
import random


# fibonacci number with index n
def fib(n: int):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)


# list of Prime numbers up to a number n
def list_prime_num(n: int) -> list:
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
def fac(n: int) -> int:
    p = 1
    for i in range(2, n+1):
        p *= i
    return p


# auxiliary function for sorting algorithm
def array_nums(length: int) -> list:
    raw_nums = []
    for i in range(1, length):
        raw_nums.append(random.randint(0, 1000000))
    return raw_nums 


# yes yes the most stupid version of bubble sort
def bubble_sort(nums: list) -> list:
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def selection_sort(nums):  
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums


cProfile.run('fib(40)')
cProfile.run('list_prime_num(5000)')
cProfile.run('fac(100000)')
cProfile.run('bubble_sort(array_nums(10000))')
cProfile.run('selection_sort(array_nums(10000))')
