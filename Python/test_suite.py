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
