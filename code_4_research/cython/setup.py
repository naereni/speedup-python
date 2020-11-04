from setuptools import setup
from Cython.Build import cythonize

# build_ext --inplace

setup(ext_modules=cythonize('D:/12/tmp/cython/main_modul.pyx'))
