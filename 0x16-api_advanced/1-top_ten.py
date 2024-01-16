#!/usr/bin/python3
"""reddit api calls"""
import requests


def top_ten(subreddit):
    """ get hot posts """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    params = {'limit': 10}
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
