#!/bin/bash
# curl a url and return the body size of response
curl -sI $1 | grep 'Content-Length:' | cut -d ' ' -f 2
