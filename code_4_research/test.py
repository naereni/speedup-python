import random
import cProfile


def array():
    nums = []
    for i in range(100):
        nums.append(i)
    return nums

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

nums = [1,5,10,15,20,25,30]
# print(array())
cProfile.run('print(binary_search(array(), 15))')

# cProfile.run('''
# ex = array()
# print(binary_search(ex[0], ex[1]))
# ''')