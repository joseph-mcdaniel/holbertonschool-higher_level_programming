#!/usr/bin/python3
#sends a request to the URL and
# displays the value of the variable X-Request-Id in the response header
import requests
from sys import argv

r = requests.get(argv[1])
print(r.headers.get("X-Request-Id"))
