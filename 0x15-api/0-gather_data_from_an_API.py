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

    tasks_done = 0
    total_tasks = 0
    for data in emp_list:
        total_tasks += 1
        if data.get('completed') is True:
            tasks_done += 1

    print(f"Employee {employee.get('name')} is done with"
          f" tasks({tasks_done}/{total_tasks}):")

    for data in emp_list:
        if data.get('completed') is True:
            print(f"\t {data.get('title')}")


if __name__ == '__main__':
    user_id = sys.argv[1]
    find_employee(user_id)
