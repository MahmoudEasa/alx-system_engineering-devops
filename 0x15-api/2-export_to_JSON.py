#!/usr/bin/python3
""" Write a Python script that, using this REST API,
    for a given employee ID,
    returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if (len(argv) == 2):
        id = int(argv[1])
        user_url = f"https://jsonplaceholder.typicode.com/users/{id}"
        user = requests.get(user_url).json()
        todo_url = f"https://jsonplaceholder.typicode.com/todos/"
        req_todo = requests.get(todo_url).json()
        todo_filter = list(filter(lambda obj: obj['userId'] == id, req_todo))
        done_filter = list(filter(lambda obj: obj['completed'], todo_filter))

        user_name = user['name']
        total_tasks = len(todo_filter)
        done_tasks = len(done_filter)

        print(f"Employee {user_name} is done with \
tasks({done_tasks}/{total_tasks}):")
        for task in done_filter:
            print("\t ", end='')
            print(task['title'])
