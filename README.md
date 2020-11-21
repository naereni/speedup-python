# Speed measurements modifications to Python with statically typed languages

### Algorithms used:
1. Fibonacci Numbers(40)
2. List of Prime numbers(5000)
3. Factorial(100000)
4. Bubble sort(10000)

--------------------------------------------------------

### **Python + libs:**
#### table by [me](https://github.com/NeonDaisy)

mode                | alg1  | alg2  | alg3  | alg4|
:----               |:----: |:----: |:----: |:---:|
vanila              | 58.62 | 0.108 | 3.107 | 7.256
PyPy3               | 10.09 | 0.032 | 10.82 | 0.239
Cython(primordial)  | 7.562 | 0.063 | 3.329 | 4.577
Cython(refactor)    | 0.341 | 0.005 | 94e-5 | 1.370
Numba(decorator)    | 0.623 | 0.018 | 0.114 | 1.823

--------------------------------------------------------

### **best Python mode vs statically typed languages**
#### table by [dereason](https://github.com/dereason)

lang | alg1 | alg2 | alg3 | alg4
:----|:----:|:----:|:----:| :----:
BPM  |
C++ (GCC Compiler)|  |  |  | 0.178
C#   |
other lang |
