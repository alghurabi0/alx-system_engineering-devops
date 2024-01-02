#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Records all tasks from all employees"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()
    json_dict = {}
    for user in users:
        user_id = user.get("id")
        json_dict[user_id] = []
        for task in todos:
            if task.get("userId") == user_id:
                json_dict[user_id].append({"username": user.get("username"),
                                           "task": task.get("title"),
                                           "completed": task.get("completed")})
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_dict, jsonfile)
