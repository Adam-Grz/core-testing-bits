import pytest
from conf import *

def test_WD_three():
	driver.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert 'Cake Solutions Ltd' in setUp().page_source

def test_WD_four():
	driver.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert 'Perhaps start by registering ...' in setUp().page_source
