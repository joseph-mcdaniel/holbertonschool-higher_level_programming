#!/usr/bin/python3
# takes in a URL and an email, sends a POST request
from sys import argv
from urllib import request, parse

values = {'email': argv[2]}
data = parse.urlencode(values)
data = data.encode('ascii')
req = request.Request(argv[1], data)


with request.urlopen(req) as response:
    html = response.read()
    print(html.decode('utf-8'))
