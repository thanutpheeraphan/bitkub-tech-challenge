import urllib, json
# import pandas as pd

url = "https://api-ropsten.etherscan.io/api?module=account&action=tokentx&address=0x4e83362442b8d1bec281594cea3050c8eb01311c&startblock=0&endblock=999999999&sort=asc&apikey=K7ST5DC6VP2Z5ZVWWD1IB3JDB5AHIEV274"

response = urllib.urlopen(url)

data = json.loads(response.read())

print (data)

