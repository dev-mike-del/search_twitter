#!/usr/bin/env python

import json
import requests
import os
import unittest
import uuid

from twitter_api_verification import auth

from search_twitter_profile import search_twitter_profile
from search_twitter_profile_followers import search_twitter_profile_followers
from search_twitter_profile_timeline import search_twitter_profile_timeline

# class TestSearchTwitterProfile(unittest.TestCase):
#     def setUp(self):
#         self.screen_name = "dev_mike_del"
#         self.search_url = (
#             'https://api.twitter.com/1.1/users/show.json?screen_name={}'.format(
#                 self.screen_name,
#                 )
#             )
#         self.results1 = requests.get(self.search_url, auth=auth).json()
#         self.results2 = search_twitter_profile(self.screen_name)

#     def test_search_twitter_profile_error(self):
#         error_screen_name = uuid.uuid4().hex
#         error_results = search_twitter_profile(error_screen_name)
#         self.assertTrue(error_results["errors"])

#     def test_search_twitter_profile_success(self):
#         success_results = search_twitter_profile(self.screen_name)
#         self.assertTrue(success_results["id"])

#     def test_search_twitter_profile_id(self):
#         self.assertEqual(self.results1["id"], self.results2['id'])
#         print(self.results1["id"], self.results2['id'])

#     def test_search_twitter_profile_id_str(self):
#         self.assertEqual(self.results1["id_str"], self.results2['id_str'])
#         print(self.results1["id_str"], self.results2['id_str'])

#     def test_search_twitter_profile_created_at(self):
#         self.assertEqual(self.results1["created_at"], self.results2["created_at"])
#         print(self.results1["created_at"], self.results2['created_at'])

#     def test_search_twitter_profile_url(self):
#         self.assertEqual(self.results1["url"], self.results2["url"])
#         print(self.results1["url"], self.results2['url'])


class TestSearchTwitterProfilefollowers(unittest.TestCase):
    def setUp(self):
        self.screen_name = "dev_mike_del"
        self.id_search_url = (
            'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name={}&count=5000'.format(
                self.screen_name
                )
            )

        self.id_results = requests.get(self.id_search_url, auth=auth).json()
        print(self.id_results)
        try:
            self.ids = self.id_results["ids"]
            self.number_of_ids = len(self.ids)
            while self.number_of_ids >= 1:
                self.set_of_ids = self.ids[:100]
                del self.ids[:100]
                self.number_of_ids = self.number_of_ids - 100
                self.user_lookup_search_url = (
                'https://api.twitter.com/1.1/users/lookup.json?user_id={}'.format(
                    "".join(str(self.set_of_ids))[1:-1],
                    )
                )

                self.user_lookup_results = requests.get(self.user_lookup_search_url,auth=auth).json()
        except Exception as e:
            raise e
        else:
            print(self.id_results)

        self.user_lookup_results2 = search_twitter_profile_followers(self.screen_name)

    def test_search_twitter_profile_followers_error(self):
        error_screen_name = uuid.uuid4().hex
        error_results = search_twitter_profile_followers(error_screen_name)
        self.assertTrue(error_results["errors"])

    def test_search_twitter_profile_followers_success(self):
        success_results = search_twitter_profile(self.screen_name)
        print(success_results)
        self.assertTrue(success_results)

    # def test_search_twitter_profile_id(self):
    #     self.assertEqual(self.results1["id"], self.results2['id'])
    #     print(self.results1["id"], self.results2['id'])

    # def test_search_twitter_profile_id_str(self):
    #     self.assertEqual(self.results1["id_str"], self.results2['id_str'])
    #     print(self.results1["id_str"], self.results2['id_str'])

    # def test_search_twitter_profile_created_at(self):
    #     self.assertEqual(self.results1["created_at"], self.results2["created_at"])
    #     print(self.results1["created_at"], self.results2['created_at'])

    # def test_search_twitter_profile_url(self):
    #     self.assertEqual(self.results1["url"], self.results2["url"])
    #     print(self.results1["url"], self.results2['url'])

if __name__ == '__main__':
    unittest.main()