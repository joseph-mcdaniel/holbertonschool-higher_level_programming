#!/usr/bin/python3
# takes in URL and email, sens POST request
from sys import argv
import requests

if __name__ == "__main__":
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
