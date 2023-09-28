#!/bin/bash
# scripts that takes a url sends request to that url
curl -s "$1" | wc -c
