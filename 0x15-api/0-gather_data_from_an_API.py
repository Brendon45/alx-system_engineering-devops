#!/usr/bin/python3
'''
Python script that returns information using REST API
First line: Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    :EMPLOYEE_NAME: name of the employee
    :NUMBER_OF_DONE_TASKS: number of completed tasks
        :TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
        of completed and non-completed tasks
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            jreq = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            alltsk = len(jreq)
            completedtsk = []
            for t in jreq:
                if t.get("completed") is True:
                    completedtsk.append(t)
            count = len(completedtsk)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, alltsk))
            for title in completedtsk:
                print("\t {}".format(title.get("title")))
