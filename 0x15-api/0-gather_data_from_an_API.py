#!/usr/bin/python3
"""
This script retrieves data from a REST API and displays information
about an employee's completed tasks.

Usage: python3 gather_data_from_an_API.py EMPLOYEE_ID

Parameters:
    EMPLOYEE_ID (int): The ID of the employee whose task information you want to retrieve.

Returns:
    None

Limitations:
    This script assumes that the employee ID is a valid integer and that the REST API is accessible.

Examples:
    $ python3 gather_data_from_an_API.py 1
    Employee Leanne Graham is done with tasks(18/20):
         sunt aut facere repellat provident occaecati excepturi optio reprehenderit
         ...
         eveniet quo quis
"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 gather_data_from_an_API.py EMPLOYEE_ID")
    sys.exit(1)

employee_id = int(sys.argv[1])

# Retrieve user information
response = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}")
if response.status_code != 200:
    print(f"Could not retrieve user information for ID {employee_id}")
    sys.exit(1)
user = response.json()
employee_name = user["name"]

# Retrieve TODO list information
response = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
if response.status_code != 200:
    print(f"Could not retrieve TODO list information for ID {employee_id}")
    sys.exit(1)
todos = response.json()

# Calculate progress
total_tasks = len(todos)
done_tasks = len([todo for todo in todos if todo["completed"]])

# Display information
print(
    f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo["completed"]:
        print(f"\t {todo['title']}")
