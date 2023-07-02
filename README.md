![py-xeger](https://i.ibb.co/6tch0qk/py-xeger-3.png)

[![CI](https://github.com/magiskboy/py-xeger/actions/workflows/ci.yml/badge.svg)](https://github.com/magiskboy/py-xeger/actions/workflows/ci.yml)
![Codecov](https://img.shields.io/codecov/c/github/magiskboy/py-xeger)
![GitHub](https://img.shields.io/github/license/magiskboy/py-xeger)
![PyPI](https://img.shields.io/pypi/v/py-xeger)
![PyPI - Downloads](https://img.shields.io/pypi/dd/py-xeger)


Library to generate random strings from regular expressions.

To install, type:

```bash
$ pip install py-xeger
```


To use, type:

```python
>>> from pyxeger import Xeger
>>> x = Xeger(limit=10)  # default limit = 10
>>> x.xeger("/json/([0-9]+)")
u'/json/15062213'
```


## About

Code adapted and refactored from the Python library [xeger](https://github.com/crdoconnor/xeger) in turn inspired by the Java library `Xeger <http://code.google.com/p/xeger/>`_.
