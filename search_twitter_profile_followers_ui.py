#!/usr/bin/env python
from search_twitter_profile_followers import search_twitter_profile_followers

def search_twitter_profile_followers_ui(twitter_handle):
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


if __name__ == "__main__":
	print("This is the UI script for search_twitter_profile_followers.py")