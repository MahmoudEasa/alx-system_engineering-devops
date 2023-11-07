#!/usr/bin/python3

"""Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not)
"""
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """Recursive function that queries the Reddit API,
        parses the title of all hot articles,
        and prints a sorted count of given keywords
        (case-insensitive, delimited by spaces.
        Javascript should count as javascript, but java should not)
    """

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'Test'}
    params = {'limit': 100, 'after': after}
    req = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if req.status_code != 200:
        return None

    try:
        posts = req.json().get('data').get('children')
        after = req.json().get('data').get('after')
        for post in posts:
            title = post.get('data').get('title')
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, after, word_dict)
