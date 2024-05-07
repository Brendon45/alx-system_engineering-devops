#!/usr/bin/python3
"""
This module defines a Python script that queries the Reddit API
to retrieve the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers for the subreddit,
             or 0 if the subreddit is invalid.
    """
	# Define the User-Agent header for the Reddit API request
	headers = {'User-Agent': 'Reddit API'}

	# Construct the URL for the subreddit's information endpoint
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

	# Send an HTTP GET request to the Reddit API with custom headers
	response = requests.get(url, headers=headers, allow_redirects=False)

	# Check if the request was successful (HTTP status code 200)
	if response.status_code == 200:
		# Parse the JSON response and extract the number of subscribers
		return response.json().get("data").get("subscribers")

	# Return 0 if the subreddit is invalid or the request failed
	return 0
