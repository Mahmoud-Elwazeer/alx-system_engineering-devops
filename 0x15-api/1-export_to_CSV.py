#!/usr/bin/python3
"""import libraries"""
import json
import csv
import requests
import sys


def main():
    """main function"""
    url = "https://jsonplaceholder.typicode.com/"
    req_personal = requests.get(url + "users/{}".format(
                sys.argv[1])).json()
    req_data = requests.get(url + "todos", params={
                "userId": sys.argv[1]}).json()

    employee_name = req_personal.get("name")
    done_tasks = list(filter(lambda x: x.get("completed") is True, req_data))

    lst = []
    for c in done_tasks:
        sub_lst = []
        sub_lst.append(c["id"])
        sub_lst.append(employee_name)
        sub_lst.append(c["completed"])
        sub_lst.append(c["title"])
        lst.append(sub_lst)

    file_name = "USER_ID.csv"

    with open(file_name, 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(lst) 


if __name__ == "__main__":
    if (len(sys.argv) != 1):
        main()
