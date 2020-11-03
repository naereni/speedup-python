### main file of vanila python
import time
# fibonacci numbers
def fib(n: int):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)

# check prime number
def is_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# list of prime num
def list_prime_num(n: int):
    res_list = []
    for num in range(1, n):
        if is_prime(num):
            res_list.append(num)
    return res_list

# factorial 
def fac(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

start = time.time()
fac(100000)
end = time.time()
print(end - start)