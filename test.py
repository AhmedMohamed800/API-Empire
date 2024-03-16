#!/usr/bin/env python3
import requests
url = 'http://api.weatherapi.com/v1/forecast.json?key=807fc75c10194ef1a6c223212241403&q=London&days=1&aqi=yes&alerts=yes'
response_ex = f'''{requests.get(url).json()}'''
print(type(eval(response_ex)))