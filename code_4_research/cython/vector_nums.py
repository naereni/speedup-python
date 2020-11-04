import random

# auxiliary function for sorting algorithm
def array(length: int):
    raw_nums = []
    for i in range(1, length):
        raw_nums.append(random.randint(0, 1000000))
    return raw_nums