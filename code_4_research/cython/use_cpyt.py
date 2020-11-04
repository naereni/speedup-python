import main_modul as mm
import cProfile
from vector_nums import array


cProfile.run('mm.fib(40)')
cProfile.run('mm.list_prime_num(5000)')
cProfile.run('mm.fac(100000)')
cProfile.run('mm.bubble_sort(array(10000))')