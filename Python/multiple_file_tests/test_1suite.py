import pytest
from conf import *

def test_WD_one():
	regbutton = 'body > div > div.ng-scope > div.row.ng-scope > div > a'
	promise = Promise(driver.get('https://cakesolutions.github.io/cake-qa-test/#/'))
	promise.then(driver.find_element_by_css_selector(regbutton).click())
	assert setUp().current_url == 'https://cakesolutions.github.io/cake-qa-test/#/register'

def test_WD_two():
	driver.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert setUp().title == 'Cake Soloptions FED Test'
