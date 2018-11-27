#!/usr/bin/env python
from search_twitter_profile_timeline import search_twitter_profile_timeline

def search_twitter_profile_timeline_ui(twitter_handle):
	timeline = search_twitter_profile_timeline(twitter_handle)

	for key in timeline:
		print("{} \n".format(key,))
		for item in key:
			print("{}: {} \n".format(item, key[item]))
	asterisks = "*"
	print('''
{}
Name: {}
Twitter handle:{}
Description: {}
Account created: {}
URL: {}
Account ID: {}
Status count: {}
Followers: {}
Following: {}
Language: {}
{}
'''.format(
	"#"*20,
	key["user"]["name"],
	key["user"]["screen_name"],
	key["user"]["description"],
	key["user"]["created_at"],
	key["user"]["entities"]["url"]["urls"][0]["expanded_url"],
	key["user"]["id_str"],
	key["user"]["statuses_count"],
	key["user"]["followers_count"],
	key["user"]["friends_count"],
	key["lang"],
	"#"*20,))