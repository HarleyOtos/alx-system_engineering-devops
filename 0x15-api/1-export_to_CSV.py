#!/usr/bin/python3
"""
A Python script to export data in the CSV format
"""
import csv
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

    # Export data to CSV format
    rows = []
    for todo in todos:
        row = [str(employee_id), employee_name,
               str(todo['completed']), todo['title']]
        row_str = ','.join(['"' + r + '"' for r in row])
        rows.append(row_str)

    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w') as file:
        file.write('\n'.join(rows))
        file.write('\n')

    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    main()
