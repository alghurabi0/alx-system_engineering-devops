#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Export to JSON"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos?userId={}".format(user_id)).json()
    username = user.get("username")
    task_list = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = username
        task_list.append(task_dict)
    json_dict = {}
    json_dict[user_id] = task_list
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(json_dict, jsonfile)
