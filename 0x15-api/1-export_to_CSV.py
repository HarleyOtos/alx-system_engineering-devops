#!/usr/bin/python3
"""
A Python script to export data in the CSV format
"""
import csv
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
    f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo["completed"]:
        print(f"\t{todo['title']}")
    else:
        print(f"\t[X] {todo['title']}")

# Export to CSV
if todos:
    with open(f"{employee_id}.csv", mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, employee_name,
                            todo["completed"], todo["title"]])
    print(f"Data exported to {employee_id}.csv")
else:
    print("No tasks found for this employee")
