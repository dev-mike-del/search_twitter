#!/usr/bin/env python

import json
import requests

from twitter_api_verification import auth

def search_twitter_profile(screen_name=False):
	if screen_name is not False:
		search_url = (
			'https://api.twitter.com/1.1/users/show.json?screen_name={}'.format(
				screen_name
				)
			)

		results = requests.get(search_url, auth=auth).json()

		for result in results:
			print("{}: {} \n".format(result, results[result]))
	else:
		pass


if __name__ == "__main__":
	search_twitter_profile("dev_mike_del")

