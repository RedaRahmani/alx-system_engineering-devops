#!/usr/bin/python3
""" Top Ten."""
import requests


def top_ten(subreddit):
    """ Top Ten."""

    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit))
    if res.status_code >= 300:
        print('None')
    else:
        for child in res.json().get("data").get("children"):
            print(child.get('data').get('title'))
