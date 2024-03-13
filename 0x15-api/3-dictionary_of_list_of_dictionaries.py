#!/usr/bin/python3
"""
A script to get data from an api
"""
import json
import requests


def get_employee_tasks(todos, employee):
    emp_list = []

    for data in todos.json():
        if data.get('userId') == employee.get('id'):
            emp_list.append({
                "username": employee.get('username'),
                "task": data.get('title'),
                "completed": data.get('completed')
                })
    return emp_list


def find_employees():
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    j_file = {}
    for user in users.json():
        tasks = get_employee_tasks(todos, user)
        j_file[user.get('id')] = tasks

    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(j_file))


if __name__ == '__main__':
    find_employees()
