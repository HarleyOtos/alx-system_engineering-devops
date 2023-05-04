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
    else:
        print("\t[X] {}".format(todo['title']))

# Export to CSV
if todos:
    with open("{}.csv".format(employee_id), mode="w", 
              newline="") as csv_file:
        writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', 
                quoting=csv.QUOTE_MINIMAL)
        for todo in todos:
            writer.writerow([
                employee_id, employee_name,
                todo["completed"], todo["title"]])
