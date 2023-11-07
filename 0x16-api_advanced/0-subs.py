#!/usr/bin/python3
"""import libraries"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers"""
    try:
        # url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

        # req = requests.get(url, allow_redirects=False).json()
        # get_data = req.get("data")
        # return (len(get_data.values()))

        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

        req = requests.get(url, allow_redirects=False).json()
        get_data = req.get("data")
        num_subscrib = get_data.get("children")[-1].get(
                "data").get("subreddit_subscribers")
        return (num_subscrib)

    except Exception:
        return (0)
