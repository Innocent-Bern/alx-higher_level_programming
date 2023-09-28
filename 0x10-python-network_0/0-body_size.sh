#!/usr/bin/env bash
# scripts that takes a url
# sends request to that url
# display the size of the body of response

curl -s "$1" | wc -c
