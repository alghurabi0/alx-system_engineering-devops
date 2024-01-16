#!/usr/bin/python3
""" qurty reddit api """
import requests


def count_words(subreddit, word_list, after=None, dic={}):
    """ advanced task alx """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            title = child.get('data').get('title')
            for word in word_list:
                ocurrences = title.lower().split().count(word.lower())
                if ocurrences > 0:
                    if word in dic:
                        dic[word] += ocurrences
                    else:
                        dic[word] = ocurrences
        if after is not None:
            return count_words(subreddit, word_list, after, dic)
        else:
            if not len(dic) > 0:
                return
            for key, value in sorted(dic.items(), key=lambda x: (-x[1], x[0])):
                print('{}: {}'.format(key.lower(), value))
    else:
        return
