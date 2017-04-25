# core-testing-bits

This repository contains installation instructions and examples in Python and JavaScript for:

• Concurrent test execution

• HTML reporting

• Fixtures

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

`pytest` is a framework which allows you to easily write and run your tests. The `xdist` extension is used for the concurrent test run, and the `html` creates html reports.

The `requests` library will help us fetch some url data.

### Example code

This chapter will showcase the concurrent test execution and the html reports generated afterwards.
```
import requests
import unittest
import re

class Test_Example_Tests(unittest.TestCase):
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

The `py.test -n auto` comes from the `pytest-xdist` library and automatically detects the number of tests to run. The `--html=report.html` generates the html report in the path specified.

#### Reporter

The result should be one test Passed and one test Failed. Open `report.html` in a browser to see the report.

##### (back to the code)

Two things to point out here:

1. The variables only exist within the scope of one test (one `def`, or method). As such there are repeated lines in the code (lines 9-10 and 13-14). There is a way to go around it, for example like this:

```
import requests
import unittest
import re

class Test_Example_Tests(unittest.TestCase):
    def setUp(self):
        response = requests.get("http://thedemosite.co.uk/")
        self.title = str(re.findall('<title>(.*?)</title>',response.text))
    def test_one(self):
        self.assertIn("FREE example PHP code", self.title)
    def test_two(self):
        self.assertIn("NOT IN THE TITLE!!!", self.title)
```
Another way, using fixtures, is described below.

2. `import re` is an unfortunate result of the limitations of the `requests` library, namely - lack of an HTML parser. The line `str(re.findall('<title>(.*?)</title>',response.text))` extracts the data from between the *title* tags and converts the data from unicode to string. The conversion is necessary for the `assertIn`, as we're comparing `string`s there.

### Fixtures

The code above can be rewritten using fixtures. Example:

```
import requests
import re
import pytest

@pytest.fixture
def abc():
    resp = requests.get("http://thedemosite.co.uk/")
    title = str(re.findall('<title>(.*?)</title>',resp.text))
    return title

def test_one(abc):
    assert ("FREE example PHP code" in abc)

def test_two(abc):
    assert ("NOT IN THE TITLE!!!" in abc)
```

The fixture is applied to the `abc` method, and the method returns `title`, which is what we want. In the two tests that we've got we call the `abc` as parameter. `abc` now has the value of `title`, ie. is a string.
Note that we've changed the `assert` command, as we're no longer using the `unittest` library.

### Helpful documentation

https://pypi.python.org/pypi/pytest-xdist

https://pypi.python.org/pypi/pytest-html

https://docs.pytest.org/en/latest/fixture.html

https://docs.python.org/2/library/unittest.html

http://docs.python-requests.org/en/master/

## JavaScript

### Installation, packages
