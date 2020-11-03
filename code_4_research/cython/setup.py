from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('D:/12/tmp/main_modul.pyx'))
