#!/usr/bin/python3
""" task02."""

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """task02."""

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit),
                       headers={"User-Agent": "custom"},
                       params={"count": count, "after": after})

    if res.status_code >= 400:
        return None

    N_hot_list = hot_list
    for child in res.json().get("data").get("children"):
        N_hot_list.append(child.get("data").get("title"))

    if not res.json().get("data").get("after"):
        return N_hot_list

    return recurse(subreddit, N_hot_list,
                   res.json().get("data").get("count"),
                   res.json().get("data").get("after"))
