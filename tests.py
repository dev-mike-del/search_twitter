#!/usr/bin/env python

import json
import requests
import os
import unittest
import uuid

from twitter_api_verification import auth

from search_twitter_profile import search_twitter_profile

class TestSearchTwitterProfile(unittest.TestCase):
    def setUp(self):
        self.twitter_handle = "dev_mike_del"
        self.search_url = (
            'https://api.twitter.com/1.1/users/show.json?screen_name={}'.format(
                self.twitter_handle,
                )
            )
        self.results1 = requests.get(self.search_url, auth=auth).json()
        self.results2 = search_twitter_profile(self.twitter_handle)

    def test_search_twitter_profile_error(self):
        error_twitter_handle = uuid.uuid4().hex
        error_results = search_twitter_profile(error_twitter_handle)
        self.assertTrue(error_results["errors"])

    def test_search_twitter_profile_success(self):
        success_results = search_twitter_profile(self.twitter_handle)
        self.assertTrue(success_results["id"])

    def test_search_twitter_profile_id(self):
        self.assertEqual(self.results1["id"], self.results2['id'])
        print(self.results1["id"], self.results2['id'])

    def test_search_twitter_profile_id_str(self):
        self.assertEqual(self.results1["id_str"], self.results2['id_str'])
        print(self.results1["id_str"], self.results2['id_str'])

    def test_search_twitter_profile_created_at(self):
        self.assertEqual(self.results1["created_at"], self.results2["created_at"])
        print(self.results1["created_at"], self.results2['created_at'])

    def test_search_twitter_profile_url(self):
        self.assertEqual(self.results1["url"], self.results2["url"])
        print(self.results1["url"], self.results2['url'])

if __name__ == '__main__':
    unittest.main()