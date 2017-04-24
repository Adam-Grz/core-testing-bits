# core-testing-bits

This repository contains installation instructions and examples in Python and JavaScript for:

• Concurrent test execution

• HTML reporting


## Python

### Installation, packages

First of all, install Python. I suggest the latest 2.x version. During the installation setup select the option that adds Python to PATH.
Then install these packages:
```
pip install pytest
pip install pytest-xdist
pip install pytest-html
pip install requests
```

`pytest` is a framework which allows you to easily write and run your tests. The `xdist` extension is used for concurrent test run, and the `html` creates html reports.

The `requests` library will help us fetch some url data.

### Example code

This chapter will showcase the concurrent test execution and the html reports generated afterwards.
```
import requests
import unittest
import re

class Test_API_Tests(unittest.TestCase):
    def setUp(self):
        print ""
    def test_one(self):
        response = requests.get("http://thedemosite.co.uk/")
        title = str(re.findall('<title>(.*?)</title>',response.text))
        self.assertIn("FREE example PHP code", title)
    def test_two(self):
        response = requests.get("http://thedemosite.co.uk/")
        title = str(re.findall('<title>(.*?)</title>',response.text))
        self.assertIn("NOT IN THE TITLE!!!", title)
```

Run the test suite with `py.test -n auto --html=report.html`

The `py.test -n auto` comes from the `pytest-xdist` library and automatically detects the number of tests to run. `--html=report.html` generates the html report in the path specified.

### Documentation

https://pypi.python.org/pypi/pytest-xdist

https://pypi.python.org/pypi/pytest-html

https://docs.python.org/2/library/unittest.html

http://docs.python-requests.org/en/master/

## JavaScript

### Installation, packages
