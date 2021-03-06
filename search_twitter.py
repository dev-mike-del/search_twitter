#!/usr/bin/env python
from search_twitter_profile_ui import search_twitter_profile_ui
from search_twitter_profile_followers_ui import search_twitter_profile_followers_ui
from search_twitter_profile_timeline_ui import search_twitter_profile_timeline_ui


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
			if search != 4:
				if twitter_handle != "":
					change_twitter_handle = input("Use the same Twitter handle: ").lower()
					if change_twitter_handle in ("no", "n"):
						twitter_handle = input("\nEnter a different Twitter handle: ")
					else:
						print("Twitter handle: {}".format(twitter_handle))
				else:
					twitter_handle = input("\nEnter a Twitter handle: ")


				if search == 1:
					search_twitter_profile_ui(twitter_handle)
				elif search == 2:
					search_twitter_profile_followers_ui(twitter_handle)
				elif search == 3:
					search_twitter_profile_timeline_ui(twitter_handle)
				elif search == 4:
					break
				elif search not in [1,2,3,4]:
					print(error_message)

		except ValueError:
			print(error_message)

