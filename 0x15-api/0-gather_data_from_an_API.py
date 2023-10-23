#!/usr/bin/python3
"""import libraries"""
import json
import requests
import sys


def main():
    """main function"""
    url = "https://jsonplaceholder.typicode.com/"
    req_personal = requests.get(url + "users/{}".format(sys.argv[1]))
    req_data = requests.get(url + "todos/{}".format(sys.argv[1]))
    
    personal_dict = json.loads(req_personal.content)
    data_dict = json.loads(req_data.content)
    
    employee_name = personal_dict.get("name")
    done_tasks = data_dict.get("userId")
    total_tasks = data_dict.get("completed")
    title = data_dict.get("title")


    print("Employee {} is done with tasks \
        ({}/{}):".format(employee_name, done_tasks, total_tasks))
    print("\t  {}".format(title))


if __name__ == "__main__":
    if (len(sys.argv) != 1):
        main()
