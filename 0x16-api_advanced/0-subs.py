#!/usr/bin/python3

"""Queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Test"}
    req = requests.get(url, headers=headers)

    if req.status_code == 200:
        return (req.json().get("data").get("subscribers"))
    else:
        return (0)
