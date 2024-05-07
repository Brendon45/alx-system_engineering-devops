#!/usr/bin/python3
"""Module with a python script(Count it!)"""
import requests
after = None
count_dictionay = []


def count_words(subreddit, word_list):
    """Method that queries Reddit api"""
    global after
    global count_dictionary
    headers = {'User-Agent': 'Reddit API'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(
            url, headers=headers, allow_redirects=False, params=params)
