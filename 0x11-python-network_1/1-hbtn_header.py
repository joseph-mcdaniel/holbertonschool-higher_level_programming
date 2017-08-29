#!/usr/bin/python3
# takes in a URL, sends a request to the URl
# displays the value of the X-Request-Id variable found in the header
from sys import argv
from urllib import request
req = request.Request(argv[1])
with request.urlopen(req) as response:
    print(response.getheader('X-Request-Id'))
