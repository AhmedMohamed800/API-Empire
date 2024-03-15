#!/usr/bin/env python3
"""apis class module"""
from models.engine.engine import DBStorage
from models.requests import Request
import requests
from bcrypt import checkpw
from datetime import datetime


class Apis:
    """the apis class"""
    __storage = None

    def __init__(self):
        """init"""
        self.__storage = DBStorage()

    def reload(self):
        """reload"""
        self.__storage.reload()

    def weather(self, function, request):
        """weather"""
        weather_api_key = '807fc75c10194ef1a6c223212241403'
        url = 'http://api.weatherapi.com/v1/'
        weather_functions = ['current', 'forecast',
                             'search', 'history']
        if not self.check_key(request.get_json().get('session-id'),
                         request.get_json().get('key')):
            raise ValueError({"Error": "Unauthorized"})
        if not function:
            raise ValueError({"Error": "No function provided"})
        if function not in weather_functions:
            raise ValueError({"Error": "Function not found"})
        if function == 'search':
            ip = self.get_ip_location(request.remote_addr)
            api_url = f'{url}{function}.json?key={weather_api_key}&q={ip}'
            response = requests.get(api_url)
        else:
            api_url = f'{url}{function}.json?key={weather_api_key}&\
                {request.query_string.decode()}'
            response = requests.get(api_url)
        if response.status_code == 200:
            self.add_req(request.get_json().get('session-id'))
        self.save_response(request, response)
        return response

    def currency(self, request):
        """currency exchange"""
        try:
            if not request.get_json().get('session-id') or\
                    not request.get_json().get('X-APIEMPIR-KEY'):
                raise ValueError({"Error": "Unauthorized"})
        except Exception:
            raise ValueError({"Error": "Unauthorized"})
        if not self.check_key(request.get_json().get('session-id'),
                              request.get_json().get('X-APIEMPIR-KEY')):
            raise ValueError({"Error": "Unauthorized"})
        key = 'access_key=m4UqvZZH7GW4UFoW'
        api_url = f'https://api.exchangeratesapi.net/v1/exchange-rates/latest?{key}'
        api_url += f'&base={request.args["base"]}'
        response = requests.get(api_url)
        if response.status_code == 200:
            self.add_req(request.get_json().get('session-id'))
        self.save_response(request, response)
        return requests.get(api_url)

    def get_ip_location(self, ip_address, requests):
        """get ip location"""
        maxmind_license_key = 'bb81035d-40d3-4d38-8b49-7502b784c41a'
        url = f'https://geolite.info/geoip/v2.1/city/\
            {ip_address}?license_key={maxmind_license_key}'
        
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['city']
        else:
            return None

    def check_key(self, session_id, key):
        """check key"""
        user = self.__storage.get('User', session_id=session_id)
        if not user.auth:
            return False
        if not checkpw(user.auth.hashed_key.encode(), key.encode()):
            return False
        if user.auth.max_req <= user.auth.used_req:
            return False
        return True
    
    def save_response(self, request, response):
        """save response"""
        user = self.__storage.get('User',
                                  session_id=request.get_json()
                                  .get('session-id'))
        req = Request(
            method=request.method,
            status_code=response.status_code,
            path=request.path,
            date=datetime.now(),
            http_version=request.environ['SERVER_PROTOCOL'],
            user_id=user.id
        )
        self.__storage.new(req)
        self.__storage.save()
    
    def add_req(self, session_id):
        """add request"""
        user = self.__storage.get('User', session_id=session_id)
        user.auth.used_req += 1
        
        self.__storage.save()
