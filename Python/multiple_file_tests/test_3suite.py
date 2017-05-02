import pytest
import requests

def test_five():
	resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert resp.status_code == 200

def test_six():
	resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert resp.headers['server'] == 'GitHub.com'

def test_seven():
	resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert resp.status_code == 200

def test_eight():
	resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')
	assert resp.status_code == 200
