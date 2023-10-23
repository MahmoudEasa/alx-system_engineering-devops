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

        user_name = user['username']
        file_name = f"{id}.csv"

        with open(file_name, 'w') as file:
            for task in todo_filter:
                file.write(f'"{task["userId"]}","{user_name}","{task["completed"]}",\
"{task["title"]}"\n')
