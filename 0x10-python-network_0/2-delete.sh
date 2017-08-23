#!/bin/bash
# sends a DELETE request to the URL passed as
# the first arg and siplays teh body of the response
curl -X DELETE "$1"
