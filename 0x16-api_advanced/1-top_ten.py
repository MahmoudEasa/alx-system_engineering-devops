#!/usr/bin/python3

"""Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ Top_ten Function """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Test"}
    params = {"limit": 10}
    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        posts = req.json().get("data").get("children")
        for post in posts:
            title = post.get('data').get('title')
            print(title)
    else:
        print(None)
