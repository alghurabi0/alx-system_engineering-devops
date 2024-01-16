#!/usr/bin/python3
"""Query reddit api"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(
            url,
            headers={"User-Agent": "My-User-Agent"},
            allow_redirects=False
            )
    if r.status_code < 300:
        return r.json().get("data").get("subscribers")
    else:
        return 0
