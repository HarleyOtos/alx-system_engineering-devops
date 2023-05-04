#!/usr/bin/python3
"""
This script retrieves data from a REST API and exports it in JSON format
"""
import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print(
            "Usage: python3 gather_data_from_an_API.py EMPLOYEE_ID")
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

    # Create the JSON data
    json_data = {}
    json_data[str(employee_id)] = [
        {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"]
        } for todo in todos
    ]

    # Write the JSON data to a file
    with open(str(employee_id) + '.json', 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    main()
