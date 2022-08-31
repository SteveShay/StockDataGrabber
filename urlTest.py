import os
import sys
#Test Script to read URL from text file.
#Funtionality used to protect API endpoints from github.

POST_URL = ""

with open(os.path.join(sys.path[0], "watchlistURL.txt")) as file:
    for line in file:
        POST_URL = line

print(POST_URL)