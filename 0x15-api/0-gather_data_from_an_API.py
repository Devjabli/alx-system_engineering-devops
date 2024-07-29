#!/usr/bin/python3
"""Access REST API to todo lists of employees"""

import requests
import sys

if __name__ == '__main__':
    empId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + empId

    res = requests.get(url, timeout=10)
    empName = res.json().get('name')

    todoUrl = url + "/todos"
    res = requests.get(todoUrl, timeout=10)
    tasks = res.json()
    done = 0
    com_tasks = []

    for task in tasks:
        if task.get('completed'):
            com_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):".
          format(empName, done, len(tasks)))

    for task in com_tasks:
        print("\t {}".format(task.get('title')))
