#!/usr/bin/env python

import datetime

from search_twitter_profile import search_twitter_profile
from search_twitter_profile_followers import search_twitter_profile_followers
from search_twitter_profile_timeline import search_twitter_profile_timeline


if __name__ == '__main__':

	search = 0

	twitter_handle = ""

	error_message = '''
Please enter the number corresponding to the search that you wish to perform
'''

	print('''
Welcome to the Python Twitter Search app created by Michael Delgado!
''')

	while search != 4:
		try:
			search = int(
				input('''
1 = Search Twitter Profile
2 = Search Twitter Profile Followers
3 = Search Twitter Profile Timeline
4 = Exit Program

''')
		)

			if twitter_handle != "":
				change_twitter_handle = input("Use the same Twitter handle: ").lower()
				if change_twitter_handle in ("no", "n"):
					twitter_handle = input("\nEnter a different Twitter handle: ")
				else:
					print("Twitter handle: {}".format(twitter_handle))
			else:
				twitter_handle = input("\nEnter a Twitter handle: ")


			if search == 1:
				profile = search_twitter_profile(twitter_handle)
				for item in profile:
					print("\n{}: {}".format(item,profile[item]))

			elif search == 2:
				followers_list = search_twitter_profile_followers(twitter_handle)
				follower_dict = {}
				verified_followers = []
				for follower in followers_list:
					follower_dict[follower["id_str"]] = {
													"name":follower["name"],
													"screen_name":follower["screen_name"],
													"verified":follower["verified"],
													"created_at":follower["created_at"],
													"favourites_count":follower["favourites_count"],
													"{} is following".format(twitter_handle):follower["following"],
													"friends_count":follower["friends_count"],
													"statuses_count":follower["statuses_count"],
													"description":follower["description"],
													"followers_count":follower["followers_count"],
													"lang":follower["lang"],
													"timestamp": datetime.datetime.now(),
													}
					try:
						follower_dict[follower["id_str"]].update({"url":follower["entities"]["url"]["urls"][0]["expanded_url"]})
					except KeyError:
						follower_dict[follower["id_str"]].update({"url":None})

					if follower["verified"] == True:
						verified_followers.append("{} (@{})".format(follower["name"],follower["screen_name"]))

				print('''
{} followers.

{} verifired followers
'''.format(len(followers_list),len(verified_followers)))

				if len(verified_followers) >= 1:
					print("Verified Followers:")
					for verified_follower in verified_followers:
						print(verified_follower)

			elif search == 3:
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


			elif search == 4:
				break
			elif search not in [1,2,3,4]:
				print(error_message)

		except ValueError:
			print(error_message)

