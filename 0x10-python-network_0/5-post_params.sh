#!/usr/bin/bash
# sends a POST requst to a given url

curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
