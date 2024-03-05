#!/usr/bin/python3
"""
A script to get data from an api
"""
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

    with open(f"{user_id}.csv", 'w') as f:
        for data in emp_list:
            uid = f"\"{user_id}\""
            uname = f"\"{employee.get('username')}\""
            tcp = f"\"{data.get('completed')}\""
            tt = f"\"{data.get('title')}\""
            f.write(f"{uid},{uname},{tcp},{tt}\n")


if __name__ == '__main__':
    user_id = sys.argv[1]
    find_employee(user_id)
