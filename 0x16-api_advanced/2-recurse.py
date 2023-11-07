#!/usr/bin/python3

"""Recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ Recurse Function """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Test"}
    params = {
            'after': after,
            'count': count
            }
    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        data = req.json().get("data")
        posts = data.get("children")

        for post in posts:
            title = post.get('data').get('title')
            hot_list.append(title)

        after = data.get('after')
        count += data.get('dist')

        if after is not None:
            return (recurse(subreddit, hot_list, after, count))

        return (hot_list)
    else:
        return (None)
