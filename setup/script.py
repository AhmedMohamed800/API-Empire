#!/usr/bin/env python3
# endpoint_title, endpoint_url, method, description, response_ex, category, api_id
import mysql.connector
from PIL import Image
import base64


THEURL = 'https://apiempire.site/api'


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
response_ex = '''{"location":{"name":"London","region":"City of London, Greater London","country":"United Kingdom","lat":51.52,"lon":-0.11,"tz_id":"Europe/London","localtime_epoch":1710585122,"localtime":"2024-03-16 10:32"},"current":{"last_updated_epoch":1710585000,"last_updated":"2024-03-16 10:30","temp_c":11.0,"temp_f":51.8,"is_day":1,"condition":{"text":"Partly cloudy","icon":"//cdn.weatherapi.com/weather/64x64/day/116.png","code":1003},"wind_mph":4.3,"wind_kph":6.8,"wind_degree":190,"wind_dir":"S","pressure_mb":1021.0,"pressure_in":30.15,"precip_mm":0.0,"precip_in":0.0,"humidity":66,"cloud":25,"feelslike_c":10.9,"feelslike_f":51.6,"vis_km":10.0,"vis_miles":6.0,"uv":3.0,"gust_mph":8.7,"gust_kph":14.0,"air_quality":{"co":283.7,"no2":22.3,"o3":56.5,"so2":11.8,"pm2_5":4.9,"pm10":6.1,"us-epa-index":1,"gb-defra-index":1}},"forecast":{"forecastday":[{"date":"2024-03-16","date_epoch":1710547200,"day":{"maxtemp_c":12.6,"maxtemp_f":54.8,"mintemp_c":6.8,"mintemp_f":44.2,"avgtemp_c":9.4,"avgtemp_f":48.9,"maxwind_mph":9.2,"maxwind_kph":14.8,"totalprecip_mm":1.68,"totalprecip_in":0.07,"totalsnow_cm":0.0,"avgvis_km":9.6,"avgvis_miles":5.0,"avghumidity":73,"daily_will_it_rain":1,"daily_chance_of_rain":91,"daily_will_it_snow":0,"daily_chance_of_snow":0,"condition":{"text":"Patchy rain nearby","icon":"//cdn.weatherapi.com/weather/64x64/day/176.png","code":1063},"uv":3.0,"air_quality":{"co":276.256,"no2":20.784000000000006,"o3":47.128,"so2":8.472000000000003,"pm2_5":4.86,"pm10":5.627999999999999,"us-epa-index":1,"gb-defra-index":1}},"astro":{"sunrise":"06:11 AM","sunset":"06:07 PM","moonrise":"08:41 AM","moonset":"01:42 AM","moon_phase":"Waxing Crescent","moon_illumination":38,"is_moon_up":1,"is_sun_up":0},"hour":[{"time_epoch":1710547200,"time":"2024-03-16 00:00","temp_c":7.6,"temp_f":45.7,"is_day":0,"condition":{"text":"Partly Cloudy ","icon":"//cdn.weatherapi.com/weather/64x64/night/116.png","code":1003},"wind_mph":7.8,"wind_kph":12.6,"wind_degree":305,"wind_dir":"NW","pressure_mb":1013.0,"pressure_in":29.92,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":80,"cloud":30,"feelslike_c":5.4,"feelslike_f":41.6,"windchill_c":5.4,"windchill_f":41.6,"heatindex_c":7.6,"heatindex_f":45.7,"dewpoint_c":4.4,"dewpoint_f":40.0,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":11.9,"gust_kph":19.2,"uv":1.0,"air_quality":{"co":260.4,"no2":11.3,"o3":52.9,"so2":3.7,"pm2_5":3.4,"pm10":3.8,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710550800,"time":"2024-03-16 01:00","temp_c":7.1,"temp_f":44.8,"is_day":0,"condition":{"text":"Overcast ","icon":"//cdn.weatherapi.com/weather/64x64/night/122.png","code":1009},"wind_mph":6.9,"wind_kph":11.2,"wind_degree":300,"wind_dir":"WNW","pressure_mb":1014.0,"pressure_in":29.96,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":83,"cloud":90,"feelslike_c":5.0,"feelslike_f":40.9,"windchill_c":5.0,"windchill_f":40.9,"heatindex_c":7.1,"heatindex_f":44.8,"dewpoint_c":4.4,"dewpoint_f":40.0,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":10.5,"gust_kph":17.0,"uv":1.0,"air_quality":{"co":260.4,"no2":12.5,"o3":45.1,"so2":3.6,"pm2_5":4.0,"pm10":4.4,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710554400,"time":"2024-03-16 02:00","temp_c":7.3,"temp_f":45.1,"is_day":0,"condition":{"text":"Cloudy ","icon":"//cdn.weatherapi.com/weather/64x64/night/119.png","code":1006},"wind_mph":6.0,"wind_kph":9.7,"wind_degree":298,"wind_dir":"WNW","pressure_mb":1015.0,"pressure_in":29.98,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":84,"cloud":71,"feelslike_c":5.5,"feelslike_f":41.8,"windchill_c":5.5,"windchill_f":41.8,"heatindex_c":7.3,"heatindex_f":45.1,"dewpoint_c":4.8,"dewpoint_f":40.6,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":8.7,"gust_kph":14.1,"uv":1.0,"air_quality":{"co":260.4,"no2":13.9,"o3":39.0,"so2":3.5,"pm2_5":4.5,"pm10":5.0,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710558000,"time":"2024-03-16 03:00","temp_c":7.4,"temp_f":45.4,"is_day":0,"condition":{"text":"Patchy rain nearby","icon":"//cdn.weatherapi.com/weather/64x64/night/176.png","code":1063},"wind_mph":5.1,"wind_kph":8.3,"wind_degree":305,"wind_dir":"NW","pressure_mb":1016.0,"pressure_in":30.01,"precip_mm":0.02,"precip_in":0.0,"snow_cm":0.0,"humidity":86,"cloud":86,"feelslike_c":5.9,"feelslike_f":42.7,"windchill_c":5.9,"windchill_f":42.7,"heatindex_c":7.4,"heatindex_f":45.4,"dewpoint_c":5.2,"dewpoint_f":41.3,"will_it_rain":1,"chance_of_rain":75,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":7.3,"gust_kph":11.8,"uv":1.0,"air_quality":{"co":260.4,"no2":14.9,"o3":34.3,"so2":3.5,"pm2_5":5.1,"pm10":5.7,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710561600,"time":"2024-03-16 04:00","temp_c":7.5,"temp_f":45.5,"is_day":0,"condition":{"text":"Patchy rain nearby","icon":"//cdn.weatherapi.com/weather/64x64/night/176.png","code":1063},"wind_mph":4.3,"wind_kph":6.8,"wind_degree":305,"wind_dir":"NW","pressure_mb":1017.0,"pressure_in":30.04,"precip_mm":0.06,"precip_in":0.0,"snow_cm":0.0,"humidity":87,"cloud":95,"feelslike_c":6.3,"feelslike_f":43.4,"windchill_c":6.3,"windchill_f":43.4,"heatindex_c":7.5,"heatindex_f":45.5,"dewpoint_c":5.5,"dewpoint_f":41.9,"will_it_rain":1,"chance_of_rain":100,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":6.2,"gust_kph":9.9,"uv":1.0,"air_quality":{"co":263.7,"no2":16.6,"o3":29.3,"so2":3.5,"pm2_5":5.7,"pm10":6.3,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710565200,"time":"2024-03-16 05:00","temp_c":7.4,"temp_f":45.4,"is_day":0,"condition":{"text":"Patchy rain nearby","icon":"//cdn.weatherapi.com/weather/64x64/night/176.png","code":1063},"wind_mph":3.6,"wind_kph":5.8,"wind_degree":320,"wind_dir":"NW","pressure_mb":1018.0,"pressure_in":30.07,"precip_mm":0.04,"precip_in":0.0,"snow_cm":0.0,"humidity":88,"cloud":75,"feelslike_c":6.6,"feelslike_f":43.9,"windchill_c":6.6,"windchill_f":43.9,"heatindex_c":7.4,"heatindex_f":45.4,"dewpoint_c":5.6,"dewpoint_f":42.0,"will_it_rain":1,"chance_of_rain":83,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":5.4,"gust_kph":8.7,"uv":1.0,"air_quality":{"co":267.0,"no2":19.5,"o3":24.0,"so2":3.6,"pm2_5":6.1,"pm10":6.9,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710568800,"time":"2024-03-16 06:00","temp_c":7.1,"temp_f":44.8,"is_day":0,"condition":{"text":"Patchy rain nearby","icon":"//cdn.weatherapi.com/weather/64x64/night/176.png","code":1063},"wind_mph":2.7,"wind_kph":4.3,"wind_degree":326,"wind_dir":"NNW","pressure_mb":1019.0,"pressure_in":30.09,"precip_mm":0.02,"precip_in":0.0,"snow_cm":0.0,"humidity":89,"cloud":72,"feelslike_c":6.7,"feelslike_f":44.1,"windchill_c":6.7,"windchill_f":44.1,"heatindex_c":7.1,"heatindex_f":44.8,"dewpoint_c":5.4,"dewpoint_f":41.7,"will_it_rain":1,"chance_of_rain":73,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":4.1,"gust_kph":6.6,"uv":1.0,"air_quality":{"co":260.4,"no2":10.8,"o3":53.6,"so2":4.3,"pm2_5":6.6,"pm10":7.5,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710572400,"time":"2024-03-16 07:00","temp_c":6.8,"temp_f":44.2,"is_day":1,"condition":{"text":"Sunny","icon":"//cdn.weatherapi.com/weather/64x64/day/113.png","code":1000},"wind_mph":2.0,"wind_kph":3.2,"wind_degree":16,"wind_dir":"NNE","pressure_mb":1020.0,"pressure_in":30.12,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":90,"cloud":16,"feelslike_c":6.8,"feelslike_f":44.3,"windchill_c":6.8,"windchill_f":44.3,"heatindex_c":6.8,"heatindex_f":44.2,"dewpoint_c":5.2,"dewpoint_f":41.4,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":3.1,"gust_kph":4.9,"uv":3.0,"air_quality":{"co":263.7,"no2":11.8,"o3":60.1,"so2":5.0,"pm2_5":5.5,"pm10":6.5,"us-epa-index":1,"gb-defra-index":1},"short_rad":20.2,"diff_rad":9.12},{"time_epoch":1710576000,"time":"2024-03-16 08:00","temp_c":7.7,"temp_f":45.9,"is_day":1,"condition":{"text":"Sunny","icon":"//cdn.weatherapi.com/weather/64x64/day/113.png","code":1000},"wind_mph":0.9,"wind_kph":1.4,"wind_degree":50,"wind_dir":"NE","pressure_mb":1021.0,"pressure_in":30.14,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":82,"cloud":13,"feelslike_c":7.7,"feelslike_f":45.9,"windchill_c":7.7,"windchill_f":45.9,"heatindex_c":7.7,"heatindex_f":45.9,"dewpoint_c":4.9,"dewpoint_f":40.8,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":1.2,"gust_kph":1.9,"uv":3.0,"air_quality":{"co":267.0,"no2":15.9,"o3":60.1,"so2":6.5,"pm2_5":4.8,"pm10":5.9,"us-epa-index":1,"gb-defra-index":1},"short_rad":83.9,"diff_rad":28.91},{"time_epoch":1710579600,"time":"2024-03-16 09:00","temp_c":8.8,"temp_f":47.8,"is_day":1,"condition":{"text":"Sunny","icon":"//cdn.weatherapi.com/weather/64x64/day/113.png","code":1000},"wind_mph":2.0,"wind_kph":3.2,"wind_degree":151,"wind_dir":"SSE","pressure_mb":1021.0,"pressure_in":30.15,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":76,"cloud":19,"feelslike_c":9.1,"feelslike_f":48.3,"windchill_c":9.1,"windchill_f":48.3,"heatindex_c":8.8,"heatindex_f":47.8,"dewpoint_c":4.8,"dewpoint_f":40.6,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":2.4,"gust_kph":3.9,"uv":3.0,"air_quality":{"co":273.7,"no2":18.3,"o3":58.7,"so2":8.5,"pm2_5":4.6,"pm10":5.8,"us-epa-index":1,"gb-defra-index":1},"short_rad":155.18,"diff_rad":46.92},{"time_epoch":1710583200,"time":"2024-03-16 10:00","temp_c":11.0,"temp_f":51.8,"is_day":1,"condition":{"text":"Partly cloudy","icon":"//cdn.weatherapi.com/weather/64x64/day/116.png","code":1003},"wind_mph":4.3,"wind_kph":6.8,"wind_degree":190,"wind_dir":"S","pressure_mb":1021.0,"pressure_in":30.15,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":66,"cloud":25,"feelslike_c":9.5,"feelslike_f":49.1,"windchill_c":9.5,"windchill_f":49.1,"heatindex_c":9.8,"heatindex_f":49.7,"dewpoint_c":4.5,"dewpoint_f":40.2,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":8.7,"gust_kph":14.0,"uv":3.0,"air_quality":{"co":283.7,"no2":22.3,"o3":56.5,"so2":11.8,"pm2_5":4.9,"pm10":6.1,"us-epa-index":1,"gb-defra-index":1},"short_rad":217.7,"diff_rad":70.17},{"time_epoch":1710586800,"time":"2024-03-16 11:00","temp_c":11.0,"temp_f":51.7,"is_day":1,"condition":{"text":"Partly Cloudy ","icon":"//cdn.weatherapi.com/weather/64x64/day/116.png","code":1003},"wind_mph":4.7,"wind_kph":7.6,"wind_degree":191,"wind_dir":"SSW","pressure_mb":1022.0,"pressure_in":30.17,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":62,"cloud":31,"feelslike_c":10.2,"feelslike_f":50.4,"windchill_c":10.2,"windchill_f":50.4,"heatindex_c":11.0,"heatindex_f":51.7,"dewpoint_c":4.0,"dewpoint_f":39.1,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":5.4,"gust_kph":8.7,"uv":4.0,"air_quality":{"co":293.7,"no2":27.4,"o3":52.2,"so2":16.2,"pm2_5":6.0,"pm10":7.2,"us-epa-index":1,"gb-defra-index":1},"short_rad":279.38,"diff_rad":82.38},{"time_epoch":1710590400,"time":"2024-03-16 12:00","temp_c":12.0,"temp_f":53.6,"is_day":1,"condition":{"text":"Partly Cloudy ","icon":"//cdn.weatherapi.com/weather/64x64/day/116.png","code":1003},"wind_mph":6.0,"wind_kph":9.7,"wind_degree":196,"wind_dir":"SSW","pressure_mb":1022.0,"pressure_in":30.17,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":55,"cloud":40,"feelslike_c":11.1,"feelslike_f":51.9,"windchill_c":11.1,"windchill_f":51.9,"heatindex_c":12.0,"heatindex_f":53.6,"dewpoint_c":3.3,"dewpoint_f":38.0,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":7.0,"gust_kph":11.2,"uv":4.0,"air_quality":{"co":300.4,"no2":30.9,"o3":45.4,"so2":19.6,"pm2_5":8.1,"pm10":9.3,"us-epa-index":1,"gb-defra-index":1},"short_rad":332.76,"diff_rad":86.02},{"time_epoch":1710594000,"time":"2024-03-16 13:00","temp_c":12.6,"temp_f":54.7,"is_day":1,"condition":{"text":"Cloudy ","icon":"//cdn.weatherapi.com/weather/64x64/day/119.png","code":1006},"wind_mph":6.9,"wind_kph":11.2,"wind_degree":193,"wind_dir":"SSW","pressure_mb":1021.0,"pressure_in":30.15,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":52,"cloud":66,"feelslike_c":11.6,"feelslike_f":52.9,"windchill_c":11.6,"windchill_f":52.9,"heatindex_c":12.6,"heatindex_f":54.7,"dewpoint_c":3.0,"dewpoint_f":37.4,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":8.0,"gust_kph":12.9,"uv":3.0,"air_quality":{"co":283.7,"no2":23.0,"o3":47.2,"so2":13.7,"pm2_5":7.7,"pm10":8.6,"us-epa-index":1,"gb-defra-index":1},"short_rad":547.58,"diff_rad":182.62},{"time_epoch":1710597600,"time":"2024-03-16 14:00","temp_c":12.6,"temp_f":54.8,"is_day":1,"condition":{"text":"Overcast ","icon":"//cdn.weatherapi.com/weather/64x64/day/122.png","code":1009},"wind_mph":8.1,"wind_kph":13.0,"wind_degree":190,"wind_dir":"S","pressure_mb":1021.0,"pressure_in":30.14,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":52,"cloud":100,"feelslike_c":11.4,"feelslike_f":52.5,"windchill_c":11.4,"windchill_f":52.5,"heatindex_c":12.7,"heatindex_f":54.8,"dewpoint_c":3.0,"dewpoint_f":37.5,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":9.4,"gust_kph":15.2,"uv":3.0,"air_quality":{"co":260.4,"no2":15.1,"o3":59.4,"so2":7.8,"pm2_5":4.5,"pm10":5.1,"us-epa-index":1,"gb-defra-index":1},"short_rad":490.32,"diff_rad":192.69},{"time_epoch":1710601200,"time":"2024-03-16 15:00","temp_c":12.2,"temp_f":53.9,"is_day":1,"condition":{"text":"Partly Cloudy ","icon":"//cdn.weatherapi.com/weather/64x64/day/116.png","code":1003},"wind_mph":8.9,"wind_kph":14.4,"wind_degree":190,"wind_dir":"S","pressure_mb":1021.0,"pressure_in":30.14,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":54,"cloud":53,"feelslike_c":10.7,"feelslike_f":51.2,"windchill_c":10.7,"windchill_f":51.2,"heatindex_c":12.2,"heatindex_f":53.9,"dewpoint_c":3.3,"dewpoint_f":37.9,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":11.0,"gust_kph":17.7,"uv":4.0,"air_quality":{"co":253.7,"no2":11.8,"o3":66.5,"so2":6.1,"pm2_5":3.4,"pm10":3.8,"us-epa-index":1,"gb-defra-index":1},"short_rad":422.58,"diff_rad":177.91},{"time_epoch":1710604800,"time":"2024-03-16 16:00","temp_c":11.5,"temp_f":52.6,"is_day":1,"condition":{"text":"Overcast ","icon":"//cdn.weatherapi.com/weather/64x64/day/122.png","code":1009},"wind_mph":9.2,"wind_kph":14.8,"wind_degree":184,"wind_dir":"S","pressure_mb":1020.0,"pressure_in":30.13,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":58,"cloud":99,"feelslike_c":9.8,"feelslike_f":49.6,"windchill_c":9.8,"windchill_f":49.6,"heatindex_c":11.5,"heatindex_f":52.6,"dewpoint_c":3.5,"dewpoint_f":38.3,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":11.8,"gust_kph":19.0,"uv":3.0,"air_quality":{"co":257.0,"no2":14.1,"o3":64.4,"so2":7.2,"pm2_5":3.4,"pm10":3.9,"us-epa-index":1,"gb-defra-index":1},"short_rad":363.14,"diff_rad":157.36},{"time_epoch":1710608400,"time":"2024-03-16 17:00","temp_c":10.7,"temp_f":51.2,"is_day":1,"condition":{"text":"Overcast ","icon":"//cdn.weatherapi.com/weather/64x64/day/122.png","code":1009},"wind_mph":8.5,"wind_kph":13.7,"wind_degree":178,"wind_dir":"S","pressure_mb":1020.0,"pressure_in":30.13,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":63,"cloud":100,"feelslike_c":8.9,"feelslike_f":48.1,"windchill_c":8.9,"windchill_f":48.1,"heatindex_c":10.7,"heatindex_f":51.2,"dewpoint_c":4.1,"dewpoint_f":39.3,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":11.2,"gust_kph":18.0,"uv":3.0,"air_quality":{"co":267.0,"no2":20.9,"o3":52.9,"so2":9.5,"pm2_5":4.5,"pm10":5.0,"us-epa-index":1,"gb-defra-index":1},"short_rad":299.89,"diff_rad":131.25},{"time_epoch":1710612000,"time":"2024-03-16 18:00","temp_c":10.1,"temp_f":50.2,"is_day":1,"condition":{"text":"Overcast ","icon":"//cdn.weatherapi.com/weather/64x64/day/122.png","code":1009},"wind_mph":8.1,"wind_kph":13.0,"wind_degree":171,"wind_dir":"S","pressure_mb":1020.0,"pressure_in":30.13,"precip_mm":0.0,"precip_in":0.0,"snow_cm":0.0,"humidity":67,"cloud":100,"feelslike_c":8.3,"feelslike_f":47.0,"windchill_c":8.3,"windchill_f":47.0,"heatindex_c":10.1,"heatindex_f":50.2,"dewpoint_c":4.3,"dewpoint_f":39.8,"will_it_rain":0,"chance_of_rain":0,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":10.8,"gust_kph":17.4,"uv":3.0,"air_quality":{"co":273.7,"no2":27.4,"o3":43.3,"so2":10.9,"pm2_5":5.2,"pm10":5.8,"us-epa-index":1,"gb-defra-index":1},"short_rad":250.53,"diff_rad":109.78},{"time_epoch":1710615600,"time":"2024-03-16 19:00","temp_c":9.8,"temp_f":49.7,"is_day":0,"condition":{"text":"Patchy rain nearby","icon":"//cdn.weatherapi.com/weather/64x64/night/176.png","code":1063},"wind_mph":8.1,"wind_kph":13.0,"wind_degree":166,"wind_dir":"SSE","pressure_mb":1020.0,"pressure_in":30.12,"precip_mm":0.01,"precip_in":0.0,"snow_cm":0.0,"humidity":69,"cloud":100,"feelslike_c":8.0,"feelslike_f":46.4,"windchill_c":8.0,"windchill_f":46.4,"heatindex_c":9.9,"heatindex_f":49.7,"dewpoint_c":4.5,"dewpoint_f":40.1,"will_it_rain":0,"chance_of_rain":61,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":11.1,"gust_kph":17.8,"uv":1.0,"air_quality":{"co":283.7,"no2":31.9,"o3":38.6,"so2":12.3,"pm2_5":5.9,"pm10":6.5,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.01},{"time_epoch":1710619200,"time":"2024-03-16 20:00","temp_c":9.9,"temp_f":49.7,"is_day":0,"condition":{"text":"Patchy rain nearby","icon":"//cdn.weatherapi.com/weather/64x64/night/176.png","code":1063},"wind_mph":7.8,"wind_kph":12.6,"wind_degree":162,"wind_dir":"SSE","pressure_mb":1020.0,"pressure_in":30.11,"precip_mm":0.01,"precip_in":0.0,"snow_cm":0.0,"humidity":70,"cloud":100,"feelslike_c":8.1,"feelslike_f":46.5,"windchill_c":8.1,"windchill_f":46.5,"heatindex_c":9.9,"heatindex_f":49.7,"dewpoint_c":4.6,"dewpoint_f":40.3,"will_it_rain":0,"chance_of_rain":70,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":11.0,"gust_kph":17.6,"uv":1.0,"air_quality":{"co":287.1,"no2":31.5,"o3":39.0,"so2":12.9,"pm2_5":6.9,"pm10":7.6,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710622800,"time":"2024-03-16 21:00","temp_c":9.4,"temp_f":48.9,"is_day":0,"condition":{"text":"Light rain","icon":"//cdn.weatherapi.com/weather/64x64/night/296.png","code":1183},"wind_mph":7.8,"wind_kph":12.6,"wind_degree":170,"wind_dir":"S","pressure_mb":1020.0,"pressure_in":30.11,"precip_mm":1.25,"precip_in":0.05,"snow_cm":0.0,"humidity":78,"cloud":100,"feelslike_c":7.5,"feelslike_f":45.4,"windchill_c":7.5,"windchill_f":45.4,"heatindex_c":9.4,"heatindex_f":48.8,"dewpoint_c":5.7,"dewpoint_f":42.3,"will_it_rain":1,"chance_of_rain":100,"will_it_snow":0,"chance_of_snow":0,"vis_km":9.0,"vis_miles":5.0,"gust_mph":11.2,"gust_kph":18.1,"uv":1.0,"air_quality":{"co":283.7,"no2":28.1,"o3":42.9,"so2":12.2,"pm2_5":6.9,"pm10":7.8,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710626400,"time":"2024-03-16 22:00","temp_c":9.5,"temp_f":49.1,"is_day":0,"condition":{"text":"Light drizzle","icon":"//cdn.weatherapi.com/weather/64x64/night/266.png","code":1153},"wind_mph":7.8,"wind_kph":12.6,"wind_degree":171,"wind_dir":"S","pressure_mb":1019.0,"pressure_in":30.1,"precip_mm":0.25,"precip_in":0.01,"snow_cm":0.0,"humidity":84,"cloud":100,"feelslike_c":7.6,"feelslike_f":45.7,"windchill_c":7.6,"windchill_f":45.7,"heatindex_c":9.5,"heatindex_f":49.1,"dewpoint_c":7.0,"dewpoint_f":44.5,"will_it_rain":1,"chance_of_rain":100,"will_it_snow":0,"chance_of_snow":0,"vis_km":2.0,"vis_miles":1.0,"gust_mph":11.8,"gust_kph":19.0,"uv":1.0,"air_quality":{"co":277.0,"no2":24.3,"o3":47.9,"so2":10.4,"pm2_5":6.7,"pm10":7.5,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0},{"time_epoch":1710630000,"time":"2024-03-16 23:00","temp_c":9.9,"temp_f":49.9,"is_day":0,"condition":{"text":"Patchy rain nearby","icon":"//cdn.weatherapi.com/weather/64x64/night/176.png","code":1063},"wind_mph":8.5,"wind_kph":13.7,"wind_degree":173,"wind_dir":"S","pressure_mb":1019.0,"pressure_in":30.09,"precip_mm":0.03,"precip_in":0.0,"snow_cm":0.0,"humidity":85,"cloud":100,"feelslike_c":8.0,"feelslike_f":46.4,"windchill_c":8.0,"windchill_f":46.4,"heatindex_c":9.9,"heatindex_f":49.9,"dewpoint_c":7.5,"dewpoint_f":45.5,"will_it_rain":1,"chance_of_rain":81,"will_it_snow":0,"chance_of_snow":0,"vis_km":10.0,"vis_miles":6.0,"gust_mph":13.2,"gust_kph":21.3,"uv":1.0,"air_quality":{"co":270.4,"no2":19.9,"o3":52.9,"so2":8.5,"pm2_5":6.1,"pm10":6.9,"us-epa-index":1,"gb-defra-index":1},"short_rad":0.0,"diff_rad":0.0}]}]},"alerts":{"alert":[]}}'''
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
