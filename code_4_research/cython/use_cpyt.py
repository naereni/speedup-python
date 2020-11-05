### testing cython moduls
import cProfile
import refactor_mod as rfm
import primordial_mod as pmm
from auxiliary_nums import array


# testing cython modul with refactoring
cProfile.run('rfm.fib(40)')
cProfile.run('rfm.list_prime_num(5000)')
cProfile.run('rfm.fac(100000)')
cProfile.run('rfm.bubble_sort(array(10000))')

# testing cython modul with refactoring
cProfile.run('pmm.fib(40)')
cProfile.run('pmm.list_prime_num(5000)')
cProfile.run('pmm.fac(100000)')
cProfile.run('pmm.bubble_sort(array(10000))')