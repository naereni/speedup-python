### main file of cython code

# fibonacci numbers
cpdef double fib(double n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

# check prime number
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