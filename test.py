#!/usr/bin/env python3
from faker import Faker
import requests
fake = Faker()

url = 'http://127.0.0.1:5000/api/currency?base=EGP'
header = {'X-APIEMPIR-KEY': '636b74fd-c328-42ad-b249-4f5a1799fd7e'}

print(requests.get(url, headers=header).json())
