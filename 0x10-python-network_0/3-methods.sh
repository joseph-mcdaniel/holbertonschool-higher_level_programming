#!/bin/bash
# displays all HTTP methods the server will accept
curl -sI OPTIONS "$1" | grep "Allow:" | cut -c 8-
