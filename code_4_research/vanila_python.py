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
def array_nums(length: int, sort: bool) -> list:
    raw_nums = [-5]
    for i in range(1, length):
        raw_nums.append(random.randint(0, 1000000))
    if sort:
        raw_nums.sort()
        random_num = random.choice(raw_nums)
        return raw_nums, random_num
    else:
        return raw_nums 


# yes yes the most stupid version of bubble sort
def bubble_sort(nums: list) -> list:
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def gen_list():
    big_list = []
    x = 1
    while len(big_list) != 10000000:
        big_list.append(x)
        x += 1
    return big_list


def binary_search(nums: list, value: int):
    mid = len(nums) // 2
    low = 0
    high = len(nums) - 1
    while nums[mid] != value and low <= high:
        if value > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return "No value"
    else:
        return mid

array_nums = array_nums(10000001, True)
nums = array_nums[0]
print(nums[0])
search_for = nums[0]
cProfile.run('print(binary_search(nums, search_for))')

# cProfile.run('fib(40)')
# cProfile.run('list_prime_num(5000)')
# cProfile.run('fac(100000)')
# cProfile.run('bubble_sort(array_nums(10000), False)')
# cProfile.run('''''')