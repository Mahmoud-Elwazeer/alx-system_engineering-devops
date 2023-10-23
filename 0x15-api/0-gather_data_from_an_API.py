#!/usr/bin/env python3
"""import libraries"""
import json
import sys
import urllib.request


def main():
    """main function"""
    url = "https://jsonplaceholder.typicode.com/todos/" + sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        # content as string and readable
        # utf_content = content.decode('utf-8')
        # convert to dict
        data = json.loads(content)
        employee_name = data.get("EMPLOYEE_NAME")
        done_tasks = data.get("NUMBER_OF_DONE_TASKS")
        total_tasks = data.get("TOTAL_NUMBER_OF_TASKS")
        content_task = data.get("TASK_TITLE")

        print("Employee {} is done with tasks \
            ({}/{}):".format(employee_name, done_tasks, total_tasks))
        print("\t  {}".format(content_task))


if __name__ == "__main__":
    if (len(sys.argv) != 1):
        main()
