#!/usr/bin/python3
"""
This Python script export data of all employees in the JSON format.
"""
import json
import requests
import sys

if len(sys.argv) != 1:
    print("Usage: python3 gather_data_from_an_API.py")
    sys.exit(1)

# Retrieve all user IDs
response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code != 200:
    print("Could not retrieve user IDs")
    sys.exit(1)
users = response.json()
user_ids = [user["id"] for user in users]

# Initialize empty dictionary to store all tasks
all_tasks = {}

# Retrieve tasks for each user
for user_id in user_ids:
    # Retrieve user information
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code != 200:
        print(f"Could not retrieve user information for ID {user_id}")
        continue
    user = response.json()
    employee_name = user["username"]

    # Retrieve TODO list information
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    if response.status_code != 200:
        print(f"Could not retrieve TODO list information for ID {user_id}")
        continue
    todos = response.json()

    # Create list of task dictionaries for the user
    task_list = []
    for todo in todos:
        task_dict = {
            "username": employee_name,
            "task": todo["title"],
            "completed": todo["completed"]
        }
        task_list.append(task_dict)

    # Add user's task list to dictionary of all tasks
    all_tasks[user_id] = task_list

# Save all tasks to JSON file
with open("todo_all_employees.json", "w") as f:
    json.dump(all_tasks, f)
