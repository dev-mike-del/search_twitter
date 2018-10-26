import json
import time
import urllib3
import requests

from requests_oauthlib import OAuth1

import keys_and_tokens

consumer_key = keys_and_tokens.consumer_key
consumer_secret = keys_and_tokens.consumer_secret
access_token = keys_and_tokens.access_token
access_token_secret = keys_and_tokens.access_token_secret

verify_credentials_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

auth = OAuth1(consumer_key, consumer_secret,
	access_token, access_token_secret)

requests.get(verify_credentials_url, auth=auth)

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


print_key_options(results)
print_results(results)
print_target_results(results)