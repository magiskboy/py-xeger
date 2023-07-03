<p align="center">
  <img width="420px" src="https://i.ibb.co/6tch0qk/py-xeger-3.png" alt='py-xeger'>
</p>
<p align="center">
    <em>String generator from Regular Expression</em>
</p>
<p align="center">
    <a href="https://github.com/magiskboy/py-xeger/actions">
        <img src="https://github.com/magiskboy/py-xeger/actions/workflows/ci.yml/badge.svg" alt="Build Status">
    </a>
    <a href="https://app.codecov.io/gh/magiskboy/py-xeger">
        <img src="https://img.shields.io/codecov/c/github/magiskboy/py-xeger" alt="Code coverage">
    </a>
    <a href="https://pypi.org/project/py-xeger/">
        <img src="https://img.shields.io/pypi/dd/py-xeger" alt="Download PyPi">
    </a>
    <a href="https://github.com/magiskboy/py-xeger/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/magiskboy/py-xeger" alt="MIT">
    </a>
    <a href="https://pypi.org/project/py-xeger/">
        <img src="https://img.shields.io/pypi/pyversions/py-xeger" alt="Py version">
    </a>
    <a href="https://pypi.org/project/py-xeger/">
        <img src="https://img.shields.io/pypi/v/py-xeger" alt="PyPi version">
    </a>
</p>

To install, type:

```bash
$ pip install py-xeger
```


To use, type:

```python
>>> from pyxeger import Xeger
>>> x = Xeger(limit=10)  # default limit = 10
>>> x.xeger("/json/([0-9]+)")
'/json/15062213'
```


## About

Code adapted and refactored from the Python library [xeger](https://github.com/crdoconnor/xeger) in turn inspired by the Java library `Xeger <http://code.google.com/p/xeger/>`_.
