#!/usr/bin/python3
"""
This Python script export data in the JSON format
"""
import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 gather_data_from_an_API.py EMPLOYEE_ID")
    sys.exit(1)

employee_id = int(sys.argv[1])

# Retrieve user information
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id))
if response.status_code != 200:
    print("Could not retrieve user information for ID " + str(
        employee_id))
    sys.exit(1)
user = response.json()
employee_name = user["name"]

# Retrieve TODO list information
response = requests.get(
    "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id))
if response.status_code != 200:
    print("Could not retrieve TODO list information for ID " + str(
        employee_id))
    sys.exit(1)
todos = response.json()

# Check if each task is in the output file, add missing tasks
filename = "{}.json".format(employee_id)
with open(filename, "r") as file:
    data = json.load(file)
tasks = data[str(employee_id)]
missing_tasks = []
for todo in todos:
    task = {"task": todo["title"],
            "completed": todo["completed"], "username": employee_name}
    if task not in tasks:
        missing_tasks.append(task)
if missing_tasks:
    tasks.extend(missing_tasks)
    data[str(employee_id)] = tasks
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Display information
if missing_tasks:
    print("Number of tasks missing: {}".format(len(missing_tasks)))
else:
    print("All tasks found: OK")
print("Data exported to {}".format(filename))
