#!/usr/bin/python3
"""Query reddit api"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0