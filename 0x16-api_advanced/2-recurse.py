#!/usr/bin/python3
""" get titles of top hot ten posts """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ get titles of top hot ten posts """
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    r = r.json()
    for post in r['data']['children']:
        hot_list.append(post['data']['title'])
    after = r['data']['after']
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
