import requests
from WatchedStock import WatchedStock as ws
import csv
import os
import sys

POST_URL = ""

with open(os.path.join(sys.path[0], "watchlistURL.txt")) as file:
    for line in file:
        POST_URL = line

headers = {"Content-Type": "application/json"}

with open('watchlist.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        wStock = ws(row[0],row[1],row[2])
        # print(wStock.to_json())
        r = requests.request("POST", POST_URL, headers=headers, data=wStock.to_json())
        print(r.text)
print("Upload Completed")