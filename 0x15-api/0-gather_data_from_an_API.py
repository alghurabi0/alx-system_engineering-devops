#!/usr/bin/python3
""" return all todos of a user """
import json
import requests
from sys import argv


base_url = "https://jsonplaceholder.typicode.com/"


if __name__ == "__main__":
    user_id = argv[1]
    user_url = '{}/users?id={}'.format(base_url, user_id)
    user = requests.get(user_url)
    userData = user.text
    userData = json.loads(userData)
    user_name = userData[0].get('name')

    todo_url = '{}/todos?userId={}'.format(base_url, user_id)
    todo = requests.get(todo_url)
    todoData = todo.text
    todoData = json.loads(todoData)
    completed = 0
    completed_tasks = []
    total_tasks = len(todoData)
    for task in todoData:
        if task.get('completed'):
            completed += 1
            completed_tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(user_name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))