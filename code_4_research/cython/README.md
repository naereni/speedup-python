### Для компила неотрефакторенного кода, эта команда
```
cythonize -a -i modulname.pyx
```

### Для компила переделанного года делаем setup.py
```python
from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('D:/12/modulname.py'))
 
# и запускаем через
# build_ext --inplace
```
