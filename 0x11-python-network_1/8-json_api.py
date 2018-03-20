#!/usr/bin/python3
# search api
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": ""}
    if len(argv) > 1:
        data["q"] = argv[1]

    r = requests.post(url, data=data)
    try:
        res = r.json()
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
