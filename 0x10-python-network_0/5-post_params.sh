#!/bin/bash
# curl a url with POST and some header variables
curl -sd 'email: hr@holbertonschool.com' -d 'subject: I will always be here for PLD' $1
