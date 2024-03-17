#!/usr/bin/env python3
import requests
session = 'f5828c84-71bf-41be-8bc8-510d4534ccc6'
key = 'b960f4e5-bb29-4c27-9e4f-c4b4424996db'
headers = {'X-APIEMPIR-KEY': key, 'session-id': session}
url = 'http://127.0.0.1:5000/api/v1/get_reqs'

data = requests.get(url, headers=headers)
print(data.json())