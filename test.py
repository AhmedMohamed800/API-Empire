#!/usr/bin/env python3
from faker import Faker
import requests
fake = Faker()

url = 'http://localhost:5000/api/weather/current?q=London'
header = {'X-APIEMPIR-KEY': '14ac4bd5-5315-4823-8ea6-b5bb70d91b57'}

print(requests.get(url, headers=header).json())
