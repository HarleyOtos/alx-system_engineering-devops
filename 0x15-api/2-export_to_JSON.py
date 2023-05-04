#!/usr/bin/python3
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

    # Create JSON object
    tasks = []
    for todo in todos:
        task = {"task": todo["title"],
                "completed": todo["completed"], "username": employee_name}
        tasks.append(task)
    data = {str(employee_id): tasks}

    # Export data in JSON format
    filename = "{}.json".format(employee_id)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    # Display information
    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    main()
