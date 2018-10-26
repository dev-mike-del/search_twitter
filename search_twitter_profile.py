#!/usr/bin/env python

import json
import time
import requests

from twitter_api_verification import auth

screen_name = "realDonaldTrump"

search_url = (
	'https://api.twitter.com/1.1/users/show.json?screen_name={}'.format(screen_name)
	)

results = requests.get(search_url, auth=auth).json()

target_keys = ["followers_count"]

def print_key_options(results):
	for x in results:
		print(x)

def print_results(results):
	for x in results:
		print("{}: {} \n".format(x, results[x]))

def print_target_results(results):
	for x in results:
		if x in target_keys:
			print("{}: {} \n".format(x, results[x]))

def search_twitter_profile():
	print_key_options(results)
	print_results(results)
	print_target_results(results)


if __name__ == "__main__":
	print_key_options(results)
	print_results(results)
	print_target_results(results)

