#!/usr/bin/python3

"""Recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit
"""
import requests


def add_list(posts, hot_list):
    """ Add posts in hot_list """
    if len(posts) == 0:
        return

    title = posts[0].get('data').get('title')

    hot_list.append(title)
    posts.pop(0)
    add_list(posts, hot_list)


def recurse(subreddit, hot_list=[], after=None):
    """ Recurse Function """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Test"}
    params = {'after': after}
    req = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if req.status_code == 200:
        data = req.json().get("data")
        posts = data.get("children")

        add_list(posts, hot_list)
        after = data.get('after')

        if after is not None:
            return (recurse(subreddit, hot_list, after))

        return (hot_list)
    else:
        return (None)
