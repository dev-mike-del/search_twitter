#!/usr/bin/env python

import json
import requests

from twitter_api_verification import auth

def search_twitter_profile_timeline(screen_name=False, number_of_tweets=1):
	if screen_name is not False:
		search_twitter_profile_timeline_url = (
			'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}'.format(
				screen_name,
				number_of_tweets,
				)
			)

		results = requests.get(search_twitter_profile_timeline_url, auth=auth).json()

		for result in results:
			print("{} \n".format(result,))
			for item in result:
				print("{}: {} \n".format(item, result[item]))
	else:
		pass


if __name__ == "__main__":
	search_twitter_profile_timeline("dev_mike_del")

