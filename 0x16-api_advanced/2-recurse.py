#!/usr/bin/python3
"""Module with a python script(recursive function)"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Method that uses recursive method to get top 10 hot titles"""
    global after
    headers = {'User-Agent': 'Reddit API'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(
            url, headers=headers, allow_redirects=False, params=params)

    if response.status_code == 200:
        next_obj = response.json().get('data').get('after')
        if next_obj is not None:
            after = next_obj
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for obj_title in list_titles:
            hot_list.append(obj_title.get('data').get('title'))
        return hot_list
    else:
        return None
