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

### Parallel run with multiple files and promises

> Update 27-04-2017

Folder `/Python/multiple_file_tests` now contains 4 test suites, a conf file, and a runner file.

The test suite files 1 and 2 contain webdriver/browser tests, 3 and 4 contain http requests tests. I've found that using this method, if the tests are mixed, some browsers close too early, resulting in `Errno 61 Connection refused`.

Let's examine the `runner.py` file:

```
import subprocess
import glob, os

def file_finder():
	count = 0
	tests = 0
	a = glob.glob("test_*.py")
	for b in a:
		f = open(b)
		contents = f.read()
		f.close()
		count = contents.count("def test_WD")
		tests = tests + count
	print tests
	return tests

prc = subprocess.Popen(["pytest", "-n %i" % file_finder(), "--html=report.html"])
prc.wait()
```

I import `subprocess` to run a command on the command line, and `glob` to find the test suite files.

The `file_finder` function searches the current directory for `test_*.py` files, and within each file it searches for tests named `test_WD`. It is important to determine the number of tests which require a browser, since that number is passed to `subprocess.Popen[...]`. This way only the correct number of browser instances will be started, so that a) there won't be any extra open windows at the end, b) each test will have a browser instance and will not prematurely end with `Connection refused`.

#### Promises

To use the Promise package, install it with `pip install promise`

In the `test_1suite.py` I'm using the Promise package this way:
```
promise = Promise(driver.get('https://cakesolutions.github.io/cake-qa-test/#/'))
promise.then(driver.find_element_by_css_selector('body > div > div.ng-scope > div.row.ng-scope > div > a').click())
```
Normally I would have used Expected Conditions and explicitly waited for an element to be visible (or presence located), before executing the next step. Promises allow you to skip explicit waits.

In the example above the URL is loaded and only after the promise is fulfilled does it click on the Registration button.


### Helpful documentation

https://pypi.python.org/pypi/pytest-xdist

https://pypi.python.org/pypi/pytest-html

https://docs.pytest.org/en/latest/fixture.html

https://docs.python.org/2/library/unittest.html

http://docs.python-requests.org/en/master/

## JavaScript (with Protractor)

### Installation, packages

To get Protractor, first install node.js.

Then run these commands:

```
npm install -g protractor
webdriver-manager update
webdriver-manager start
```

This installs the Protractor globally and starts up a Selenium server.

### Example code

Concurrent test execution has not been implemented in Protractor very well. There is one way that I've found to run your tests in parallel, which involves scripting **one test per one file**.

Create a starter file, eg. `run.js`

Use this config:
```
var fs = require('fs');
var files = fs.readdirSync('./test/specs');

exports.config = {
  framework: 'jasmine',
  seleniumAddress: 'http://localhost:4444/wd/hub',
  specs: ['./test/specs/test_*.js'],
  jasmineNodeOpts: {
    showColors: true,
  },
  multiCapabilities: [{
        browserName: 'chrome',
        shardTestFiles: true,
        maxInstances: files.length,
    }]
};
```

The tests are located in `./test/specs`, but they can be located anywhere else, as long as the path in `run.js` is correct.

The key here is `multiCapabilities`. That option will run the tests concurrently, but make sure that `maxInstances == number of your tests`. Hence it is good to use the `files.legth` there.

There are two tests in test/specs and a page object file in test/pageObjects. The tests are simple (copied from protractortest.org) and only serve a purpose of showcasing the concurrent execution.

Start protractor with `protractor run.js`. Two Chrome windows should open (one on top of the other, but there are two) and the tests will be executed simultaneously.

### Helpful documentation

http://www.protractortest.org/#/
