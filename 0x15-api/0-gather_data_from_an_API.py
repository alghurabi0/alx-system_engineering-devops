#!/usr/bin/python3
""" return all todos of a user """
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos', params={'userId': user_id}).json()
    completed = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                          len(completed),
                                                          len(todos)))
    for task in completed:
        print("\t {}".format(task.get('title')))
