#!usr/bin/python3
"""Returns to do list for a given employee ID"""

import requests
import sys

if __name__ = "__main__":
    url = "http://jsonplaceholder.typicode.com/"
    user =  request.get(url + "users/{}".format(sys.argv[1])).json()
    todos = request.get(url + "todos", params = {"userid" : sys.argv[1]}).json()

completed = [t.get("title") for t in todos if t.get ("completed") is True]
print ("Employee {} is done with task ({}/{}):".format(
    user.get("name"), len(completed), len(todos)))
[print ("\t{})".format(c)) for c in completed]