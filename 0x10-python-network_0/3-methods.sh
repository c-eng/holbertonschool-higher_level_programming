#!/bin/bash
# curl a url and return allowed requests
curl -sI $1 | grep 'Allow:' | cut -d ' ' -f 2-
