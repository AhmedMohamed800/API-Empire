#!/usr/bin/env python3
# endpoint_title, endpoint_url, method, description, response_ex, category, api_id
import mysql.connector
from PIL import Image
import base64
import requests


THEURL = 'https://apiempire.site/api'
url = 'http://api.weatherapi.com/v1/forecast.json?key=807fc75c10194ef1a6c223212241403&q=London&days=1&aqi=yes&alerts=yes'


# Establish connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="api_user",
    password="password",
    database="api_db"
)

cursor = connection.cursor()

# Define data
title = "Weather API"
description = "WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy."
category = "weather"
image_cover = Image.open("image.jpg")
with open("image.jpg", "rb") as image_file:
    image = f'data:image/{image_cover.format};base64,{base64.b64encode(image_file.read()).decode()}'
# Insert data into the table
insert_query = "INSERT INTO API (title, description, category, image_cover) VALUES (%s, %s, %s, %s)"
cursor.execute(insert_query, (title, description, category, image))
endpoint_title = 'current'
endpoint_url = f'{THEURL}/weather/current?city=city&aqi=(yes,no)'
method = 'GET'
description = 'Get the current weather for a city.\
    takes from query parameter city like ?q=city\
        takes aqi parameter to get air quality index like ?q=city&aqi=yes'
response_ex = """{
body:{
    "location": {
        "name": "Alexandria",
        "region": "Al Iskandariyah",
        "country": "Egypt",
        "lat": 31.2,
        "lon": 29.92,
        "tz_id": "Africa/Cairo",
        "localtime_epoch": 1710456336,
        "localtime": "2024-03-15 0:45"
    },
    "current": {
        "last_updated_epoch": 1710456300,
        "last_updated": "2024-03-15 00:45",
        "temp_c": 13.0,
        "temp_f": 55.4,
        "is_day": 0,
        "condition": {
            "text": "Clear",
            "icon": "//cdn.weatherapi.com/weather/64x64/night/113.png",
            "code": 1000
        },
        "wind_mph": 3.8,
        "wind_kph": 6.1,
        "wind_degree": 150,
        "wind_dir": "SSE",
        "pressure_mb": 1017.0,
        "pressure_in": 30.03,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 77,
        "cloud": 0,
        "feelslike_c": 12.2,
        "feelslike_f": 53.9,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 1.0,
        "gust_mph": 10.4,
        "gust_kph": 16.8
    }
}
"""
category = "weather"
cursor.execute("SELECT id FROM API WHERE title = 'Weather API'")
api_id = cursor.fetchone()[0]
_ = cursor.fetchall()
cursor.execute(
    "INSERT INTO endpoint (title, url, method, description, response_ex, category, api_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    (endpoint_title,
     endpoint_url,
     method,
     description,
     response_ex,
     category,
     api_id))
endpoint_title = 'forecast'
endpoint_url = f'{THEURL}/weather/forecast?q=city&days=int&aqi=(yes,no)&alerts=(yes,no)'
method = 'GET'
description = 'Get the 5 day weather forecast for a city.\
    takes from query parameter city like ?q=city\
        takes aqi parameter to get air quality index like ?q=city&aqi=yes\
            takes days parameter to get the forecast for the next 1 to 10 days like ?q=city&days=5\
                takes hour parameter to get the forecast for every hour like ?q=city&hour=24\
                    takes language parameter to get the forecast in the language like ?q=city&lang=ar\
                        takes the date parameter to get the forecast for a specific date like ?q=city&dt=2024-03-15\
                            takes the timezone parameter to get the forecast in the timezone like ?q=city&tz=Europe/London\
                                takes the alerts parameter to get the weather alerts like ?q=city&alerts=yes'
response_ex = f'''{requests.get(url).json()}'''
cursor.execute(
    "INSERT INTO endpoint (title, url, method, description, response_ex, category, api_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    (endpoint_title,
     endpoint_url,
     method,
     description,
     response_ex,
     category,
     api_id))
title = "exchange rate"
description = "Get the latest foreign exchange reference rates in JSON format."
category = "finance"
image_cover = Image.open("image1.png")
with open("image1.png", "rb") as image_file:
    image = f'data:image/{image_cover.format};base64,{base64.b64encode(image_file.read()).decode()}'
# Insert data into the table
insert_query = "INSERT INTO API (title, description, category, image_cover) VALUES (%s, %s, %s, %s)"
cursor.execute(insert_query, (title, description, category, image))
endpoint_title = "exchange rate"
description = "get the least exchange rate for a currency"
endpoint_url = f"{THEURL}/currency?base=EGP"
response_ex = """{
  "base": "EGP",
  "date": "2024-03-15",
  "rates": {
    "AED": 0.076812,
    "AFN": 1.497018,
    "ALL": 1.993177,
    "AMD": 8.474607,
    "ANG": 0.037919,
    "AOA": 17.415712,
    "ARS": 17.784198,
    "AUD": 0.031842,
    "AWG": 0.03765,
    "AZN": 0.035643,
    "BAM": 0.03761,
    "BBD": 0.042484,
    "BDT": 2.309124,
    "BGN": 0.037553,
    "BHD": 0.007884,
    "BIF": 60.166437,
    "BMD": 0.020916,
    "BND": 0.028018,
    "BOB": 0.1454,
    "BRL": 0.104365,
    "BSD": 0.021041,
    "BTC": 0,
    "BTN": 1.742096,
    "BWP": 0.285294,
    "BYN": 0.068847,
    "BYR": 409.962081,
    "BZD": 0.042412,
    "CAD": 0.028299,
    "CDF": 57.896688,
    "CHF": 0.018451,
    "CLF": 0.000711,
    "CLP": 19.617947,
    "CNY": 0.150517,
    "COP": 81.429764,
    "CRC": 10.745655,
    "CUC": 0.020916,
    "CUP": 0.554285,
    "CVE": 2.120421,
    "CZK": 0.48331,
    "DJF": 3.746749,
    "DKK": 0.143183,
    "DOP": 1.243404,
    "DZD": 2.811162,
    "EGP": 1,
    "ERN": 0.313746,
    "ETB": 1.194704,
    "EUR": 0.019201,
    "FJD": 0.046848,
    "FKP": 0.016408,
    "GBP": 0.016399,
    "GEL": 0.055432,
    "GGP": 0.016408,
    "GHS": 0.271435,
    "GIP": 0.016408,
    "GMD": 1.421276,
    "GNF": 180.836095,
    "GTQ": 0.164281,
    "GYD": 4.401992,
    "HKD": 0.163609,
    "HNL": 0.518094,
    "HRK": 0.143955,
    "HTG": 2.789486,
    "HUF": 7.549881,
    "IDR": 326.758604,
    "ILS": 0.076485,
    "IMP": 0.016408,
    "INR": 1.732781,
    "IQD": 27.562182,
    "IRR": 879.222244,
    "ISK": 2.85489,
    "JEP": 0.016408,
    "JMD": 3.257733,
    "JOD": 0.014828,
    "JPY": 3.109175,
    "KES": 2.813168,
    "KGS": 1.872223,
    "KHR": 85.072973,
    "KMF": 9.458478,
    "KPW": 18.824264,
    "KRW": 27.827118,
    "KWD": 0.006429,
    "KYD": 0.017534,
    "KZT": 9.423793,
    "LAK": 437.676353,
    "LBP": 1872.020724,
    "LKR": 6.429125,
    "LRD": 4.029556,
    "LSL": 0.392593,
    "LTL": 0.061761,
    "LVL": 0.012652,
    "LYD": 0.100504,
    "MAD": 0.210944,
    "MDL": 0.370829,
    "MGA": 94.687911,
    "MKD": 1.181107,
    "MMK": 44.184487,
    "MNT": 71.039773,
    "MOP": 0.169523,
    "MRU": 0.834665,
    "MUR": 0.961752,
    "MVR": 0.322056,
    "MWK": 35.202353,
    "MXN": 0.348691,
    "MYR": 0.098401,
    "MZN": 1.328434,
    "NAD": 0.392383,
    "NGN": 33.262361,
    "NIO": 0.769753,
    "NOK": 0.221275,
    "NPR": 2.787377,
    "NZD": 0.034291,
    "OMR": 0.008052,
    "PAB": 0.021041,
    "PEN": 0.077348,
    "PGK": 0.08036,
    "PHP": 1.161531,
    "PKR": 5.83568,
    "PLN": 0.08241,
    "PYG": 153.704402,
    "QAR": 0.076146,
    "RON": 0.095442,
    "RSD": 2.250587,
    "RUB": 1.916887,
    "RWF": 26.940365,
    "SAR": 0.078444,
    "SBD": 0.175629,
    "SCR": 0.280845,
    "SDG": 8.774274,
    "SEK": 0.21607,
    "SGD": 0.027962,
    "SHP": 0.026632,
    "SLE": 0.475774,
    "SLL": 475.774199,
    "SOS": 11.952609,
    "SRD": 0.737649,
    "STD": 432.927927,
    "SVC": 0.184107,
    "SYP": 271.948694,
    "SZL": 0.391424,
    "THB": 0.748526,
    "TJS": 0.230391,
    "TMT": 0.073417,
    "TND": 0.064768,
    "TOP": 0.04944,
    "TRY": 0.673853,
    "TTD": 0.142859,
    "TWD": 0.661342,
    "TZS": 53.472918,
    "UAH": 0.813958,
    "UGX": 81.747708,
    "USD": 0.020916,
    "UYU": 0.816392,
    "UZS": 264.410801,
    "VEF": 75755.11268,
    "VES": 0.757838,
    "VND": 517.054217,
    "VUV": 2.499761,
    "WST": 0.057288,
    "XAF": 12.613972,
    "XAG": 0.00083,
    "XAU": 1e-05,
    "XCD": 0.056528,
    "XDR": 0.015753,
    "XOF": 12.613972,
    "XPF": 2.29131,
    "YER": 5.23642,
    "ZAR": 0.39014,
    "ZMK": 188.272934,
    "ZMW": 0.523911,
    "ZWL": 6.735083
  },
  "success": true,
  "timestamp": 1710534426778
}
"""
cursor.execute('SELECT id FROM API WHERE title = "exchange rate"')
id = cursor.fetchone()[0]
_ = cursor.fetchall()
cursor.execute(
    "INSERT INTO endpoint (title, url, method, description, response_ex, category, api_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    (endpoint_title,
     endpoint_url,
     method,
     description,
     response_ex,
     category,
     id))
connection.commit()
cursor.close()
connection.close()
