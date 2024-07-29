#!/usr/bin/python3
"""Access REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    empId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + empId

    res = requests.get(url, timeout=10)
    username = res.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl, timeout=10)
    tasks = response.json()

    dictionary = {empId: []}
    for task in tasks:
        dictionary[empId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(empId), 'w') as filename:
        json.dump(dictionary, filename)
