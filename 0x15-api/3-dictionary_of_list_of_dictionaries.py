#!/usr/bin/python3
"""Access REST API to todo lists of employees"""

import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url, timeout=10)
    users = res.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        res = requests.get(url, timeout=10)
        tasks = res.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
