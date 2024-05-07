#!/usr/bin/python3
"""Module defines a Python script that queries the Reddit API
to retrieve the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers or 0 if subreddit is invalid.
    """
    headers = {'User-Agent': 'Reddit API'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
