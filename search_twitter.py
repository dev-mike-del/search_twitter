#!/usr/bin/env python

from search_twitter_profile import search_twitter_profile
from search_twitter_profile_followers import search_twitter_profile_followers
from search_twitter_profile_timeline import search_twitter_profile_timeline


if __name__ == '__main__':

print('''
Welcome to the Python Twitter Search app created by Michael Delgado!
''')

search = 0

while search != 4:
	search = int(
		input('''
1 = Search Twitter Profile
2 = Search Twitter Profile Followers
3 = Search Twitter Profile Timeline
4 = Exit Program
''')
		)

	if search == 1:
		search_twitter_profile(input("Twitter handle: "))
	elif search == 2:
		search_twitter_profile_followers(input("Twitter handle: "))
	elif search == 3:
		search_twitter_profile_timeline(input("Twitter handle: "))
	elif search == 4 or search.lower() == "exit":
		break
	else:
		print('''
Please enter the number corresponding to the search that you wish to perform
''')