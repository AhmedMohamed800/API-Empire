#!/usr/bin/env python3
import mysql.connector
from PIL import Image
import base64

#Establish connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="api_user",
    password="password",
    database="api_db"
)

cursor = connection.cursor()

#Define data
title = "Weather API"
description = "WeatherAPI.com provides access to weather and geo data via a JSON/XML restful API. It allows developers to create desktop, web and mobile applications using this data very easy."
category = "weather"
image_cover = Image.open("image.jpg")
with open("image.jpg", "rb") as image_file:
    image = f'data:image/{image_cover.format};base64,{base64.b64encode(image_file.read()).decode()}'
#Insert data into the table
insert_query = "INSERT INTO API (title, description, category, image_cover) VALUES (%s, %s, %s, %s)"
cursor.execute(insert_query, (title, description, category, image))

connection.commit()
cursor.close()
connection.close()
