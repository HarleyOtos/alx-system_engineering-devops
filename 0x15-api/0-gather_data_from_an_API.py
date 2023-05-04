#!/usr/bin/python3
"""
This script retrieves data from a REST API and
displays information about an employee's completed tasks.
"""

import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Retrieve user information
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id))
    if response.status_code != 200:
        print("Could not retrieve user information for ID " 
              + str(employee_id))
        sys.exit(1)
    user = response.json()
    employee_name = user["name"]

    # Retrieve TODO list information
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(employee_id))
    if response.status_code != 200:
        print("Could not retrieve TODO list information for ID " 
              + str(employee_id))
        sys.exit(1)
    todos = response.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo["completed"]])

    # Display information
    print(
        "Employee {} is done with tasks({}/{})".format(
            employee_name, done_tasks, total_tasks))
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo['title']))


if __name__ == "__main__":
    main()
