#!/usr/bin/env python

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
				results = search_twitter_profile(twitter_handle)
				for result in results:
					print("\n{}: {}".format(result,results[result]))
			elif search == 2:
				search_twitter_profile_followers(twitter_handle)
				# results = search_twitter_profile_followers(twitter_handle)
				# for result in results:
				# 	print("\n"*5)
				# 	for item in result:
				# 		print("{}: {}".format(item, result[item]))
				# asterisks = "*"*(
				# 	len(twitter_handle)+int(len(str(len(result))))+15
				# 	)
				# print("\n{}\n{} has {} followers\n{}".format(
				# 	asterisks, twitter_handle, len(results), asterisks))
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

