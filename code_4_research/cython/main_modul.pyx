### main file of cython code

# fibonacci numbers
cpdef double fib(double n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)


# auxiliary function for list_prime_num()
cpdef is_prime(int n):
    cdef int i
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# list of prime num
cpdef list list_prime_num(int n):
    cdef list res_list = []
    cdef int num 
    for num in range(1, n):
        if is_prime(num):
            res_list.append(num)
    return res_list


# factorial
cpdef int fac(int n):
    cdef int p = 1
    cdef int i
    for i in range(2, n+1):
        p *= i
    return p


# yes yes the most stupid version of bubble sort
cpdef list bubble_sort(list nums):
    cdef int i
    cdef int j
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums