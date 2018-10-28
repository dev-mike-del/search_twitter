#!/usr/bin/env python

from search_twitter_profile import search_twitter_profile
from search_twitter_profile_followers import search_twitter_profile_followers
from search_twitter_profile_timeline import search_twitter_profile_timeline


if __name__ == '__main__':

	search = 0

	print('''
Welcome to the Python Twitter Search app created by Michael Delgado!
''')

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
			search_twitter_profile(input("\nTwitter handle: "))
		elif search == 2:
			search_twitter_profile_followers(input("\nTwitter handle: "))
		elif search == 3:
			search_twitter_profile_timeline(input("\nTwitter handle: "))
		elif search == 4:
			break
		else:
			print('''
Please enter the number corresponding to the search that you wish to perform
''')