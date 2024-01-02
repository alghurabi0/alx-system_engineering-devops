#!/usr/bin/python3
""" return all todos of a user """
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user = requests.get(url + 'users/{}'.format(user_id))
    userData = user.text
    userData = json.loads(userData)
    userName = userData.get('name')
    todos = requests.get(url + 'todos', params={'userId': user_id})
    tasks = todos.text
    tasks = json.loads(tasks)
    completed = [task for task in tasks if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(userName,
                                                          len(completed),
                                                          len(tasks)))
    for task in completed:
        print("\t {}".format(task.get('title')))
