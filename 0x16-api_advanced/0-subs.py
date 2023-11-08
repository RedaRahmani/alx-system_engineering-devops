#!/usr/bin/python3
""" This script return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers"""

    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit))
    if res.status_code >= 300:
        return 0

    return res.json().get("data").get("subscribers")
