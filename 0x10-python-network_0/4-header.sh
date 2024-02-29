#!/bin/bash
#  takes in a URL as an argument, sends a GET request to the URL and displays response
curl -sX GET -H "X-School-User-Id: 98" "$1"
