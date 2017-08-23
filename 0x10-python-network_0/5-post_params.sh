#!/bin/bash
# takes URL, sends a POST request passed to URL
curl -sd "email=hr@holbertonschool.com" -sd "subject=I will always be here for PLD" "$1"
