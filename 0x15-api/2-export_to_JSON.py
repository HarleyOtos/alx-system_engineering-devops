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
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
if response.status_code != 200:
    print(f"Could not retrieve user information for ID {employee_id}")
    sys.exit(1)
user = response.json()
employee_name = user["name"]

# Retrieve TODO list information
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
if response.status_code != 200:
    print(f"Could not retrieve TODO list information for ID {employee_id}")
    sys.exit(1)
todos = response.json()

# Create JSON object
tasks = []
for todo in todos:
    task = {"task": todo["title"], "completed": todo["completed"], "username": employee_name}
    tasks.append(task)
data = {str(employee_id): tasks}

# Export data in JSON format
filename = f"{employee_id}.json"
with open(filename, "w") as file:
    json.dump(data, file, indent=4)

# Display information
print(f"Data exported to {filename}")
