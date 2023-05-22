#!/usr/bin/python3
"""REST API for todo lists of employees"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_response.raise_for_status()
        todo_response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        sys.exit(1)

    employee_name = user_response.json().get("name")
    tasks = todo_response.json()
    completed_tasks = [task for task in tasks if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(tasks)}):")

    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Please provide a valid employee ID as a parameter.")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
