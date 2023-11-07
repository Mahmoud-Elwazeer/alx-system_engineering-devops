#!/usr/bin/python3
"""import libraries"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers"""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

        req = requests.get(url).json()
        get_data = req.get("data")
        return (len(get_data.values()))

    except Exception:
        return (0)
