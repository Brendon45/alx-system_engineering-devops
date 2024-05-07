#!/usr/bin/python3
"""Module with a python script"""
import requests


def top_ten(subreddit):
    """Query the top 10 hot post title"""
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "MyRedditBot"}
        response = requests.get(url, headers=headers)
        data = response.json()
        for i in range(10):
            print(data["data"]["children"][i]["data"]["title"])
        return data["data"]
    except Exception:
        print("None")
