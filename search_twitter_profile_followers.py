#!/usr/bin/env python

import json
import requests

from twitter_api_verification import auth

def search_twitter_profile_followers(screen_name=False):
	if screen_name is not False:
		id_search_url = (
			'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name={}&count=5000'.format(
				screen_name
				)
			)

		id_results = requests.get(id_search_url, auth=auth).json()
		ids = id_results["ids"]
		number_of_ids = len(ids)

		while number_of_ids >= 1:
			set_of_ids = ids[:100]
			del ids[:100]
			number_of_ids = number_of_ids - 100
			user_lookup_search_url = (
			'https://api.twitter.com/1.1/users/lookup.json?user_id={}'.format(
				"".join(str(set_of_ids))[1:-1],
				)
			)

			user_lookup_results = requests.get(user_lookup_search_url,auth=auth).json()

			for user in user_lookup_results:
				print('''
Twitter Handle: @{}
Name: {}
Verified: {}
Followers: {}
location: {}
'''.format(
			user["screen_name"],
			user["name"],
			user["verified"],
			user["followers_count"],
			user["location"]
		)
)

	else:
		pass


if __name__ == "__main__":
	search_twitter_profile_followers("dev_mike_del")

