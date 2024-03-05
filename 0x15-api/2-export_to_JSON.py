#!/usr/bin/python3
"""
A script to get data from an api
"""
import json
import requests
import sys


def find_employee(user_id):
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    emp_list = []
    for data in todos.json():
        if data.get('userId') == int(user_id):
            emp_list.append(data)
    if len(emp_list) == 0:
        return

    employee = None
    for data in users.json():
        if data.get('id') == int(user_id):
            employee = data
            break
    if employee is None:
        return

    with open(f"{user_id}.json", 'w') as f:
        uid = f"{user_id}"
        j_file = {f"{uid}": None}
        tasks_list = []

        for data in emp_list:
            uname = f"{employee.get('username')}"
            tcp = data.get('completed')
            tt = f"{data.get('title')}"
            tasks_list.append({
                "task": tt,
                "completed": tcp,
                "username": uname,
                })
        j_file[f'{uid}'] = tasks_list
        f.write(json.dumps(j_file))


if __name__ == '__main__':
    user_id = sys.argv[1]
    find_employee(user_id)
