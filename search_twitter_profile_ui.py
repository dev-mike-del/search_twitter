#!/usr/bin/env python

from search_twitter_profile import search_twitter_profile


def search_twitter_profile_ui(twitter_handle):
	profile = search_twitter_profile(twitter_handle)
	for item in profile:
		print("\n{}: {}".format(item,profile[item]))


if __name__ == "__main__":
	print("This is the UI script for search_twitter_profile.py")
