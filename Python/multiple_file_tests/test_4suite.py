import pytest
import requests

def test_nine():
	resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert resp.status_code == 200

def test_ten():
	resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert resp.status_code == 200

def test_eleven():
	resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert resp.status_code == 200
