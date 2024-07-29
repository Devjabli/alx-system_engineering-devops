#!/usr/bin/python3
"""Access REST API for todo lists of employees"""

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

    with open('{}.csv'.format(empId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(empId, username, task.get('completed'),
                               task.get('title')))
