#!/usr/bin/python3
""" Write a Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import json
    import requests

    users_url = f"https://jsonplaceholder.typicode.com/users/"
    users = requests.get(users_url).json()
    todos_url = f"https://jsonplaceholder.typicode.com/todos/"
    todos = requests.get(todos_url).json()

    file_name = f"todo_all_employees.json"
    tasks = {}

    for user in users:
        tasks[user['id']] = []

        for task in todos:
            if (task['userId'] == user['id']):
                obj = {
                        "username": user['username'],
                        "task": task['title'],
                        "completed": task['completed'],
                }
                tasks[user['id']].append(obj)

    with open(file_name, 'w') as file:
        json.dump(tasks, file)
