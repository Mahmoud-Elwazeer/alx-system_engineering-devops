#!/usr/bin/python3
"""import libraries"""
import csv
import json
import requests
import sys


def main():
    """main function"""
    url = "https://jsonplaceholder.typicode.com/"
    req_personal = requests.get(url + "users?id={}".format(
                sys.argv[1])).json()
    req_data = requests.get(url + "todos", params={
                "userId": sys.argv[1]}).json()

    employee_name = req_personal.get("username")

    lst = []
    lst.append(sys.argv[1])
    for c in req_data:
        sub_dct = {}
        sub_dct["task"] = c.get("title")
        sub_dct["completed"] = c.get("completed")
        sub_dct["username"] = employee_name
        lst.append(sub_dct)

    file_name = "{}.json".format(sys.argv[1])

    with open(file_name, 'w') as json_file:
        json.dump(lst, json_file, indent=4)


if __name__ == "__main__":
    if (len(sys.argv) != 1):
        main()
