#!/usr/bin/env python3
"""apis class module"""
from models.engine.engine import DBStorage
from models.requests import Request
import requests
from datetime import datetime


class ApisEngine:
    """A class that represents the APIs engine.

    This class provides methods for handling weather and currency\
        exchange APIs.

    Attributes:
        __storage (DBStorage):\
            An instance of the DBStorage class for data storage.

    """

    __storage = None

    def __init__(self):
        """Initialize the ApisEngine class."""
        self.__storage = DBStorage()

    def reload(self):
        """Reload the data storage."""
        self.__storage.reload()

    def weather(self, function, request):
        """Handle weather API requests.

        Args:
            function (str): The weather function to be executed.
            request (Request): The request object containing the\
                API request details.

        Returns:
            Response: The response object containing the weather API response.

        Raises:
            ValueError: If the request is unauthorized,\
                no function is provided, or the function is not found.

        """
        weather_api_key = '807fc75c10194ef1a6c223212241403'
        url = 'http://api.weatherapi.com/v1/'
        weather_functions = ['current', 'forecast', 'search', 'history']

        if not self.check_key(request.headers.get('X-APIEMPIR-KEY')):
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
            para = f'?key={weather_api_key}&{request.query_string.decode()}'
            api_url = f'{url}{function}.json{para}'
            response = requests.get(api_url)

        if response.status_code == 200:
            self.add_req(request.headers.get('X-APIEMPIR-KEY'))

        self.save_response(request, response)
        return response

    def currency(self, request):
        """Handle currency exchange API requests.

        Args:
            request (Request): The request object containing\
                the API request details.

        Returns:
            Response: The response object containing the currency\
                exchange API response.

        Raises:
            ValueError: If the request is unauthorized.

        """
        try:
            if not request.headers.get('X-APIEMPIR-KEY'):
                raise ValueError("Unauthorized")
        except Exception:
            print("here?")
            raise ValueError("Unauthorized")

        if not self.check_key(request.headers.get('X-APIEMPIR-KEY')):
            raise ValueError("Unauthorized")
        key = 'access_key=m4UqvZZH7GW4UFoW'
        api_url =\
                f'https://api.exchangeratesapi.net/v1/exchange-rates/latest?{key}'
        api_url += f'&base={request.args["base"]}'
        response = requests.get(api_url)

        if response.status_code == 200:
            self.add_req(request.headers.get('X-APIEMPIR-KEY'))

        self.save_response(request, response)
        return requests.get(api_url)

    def get_ip_location(self, ip_address, requests):
        """Get the location based on the IP address.

        Args:
            ip_address (str): The IP address.
            requests: The requests object.

        Returns:
            str: The city name based on the IP address.

        """
        maxmind_license_key = 'bb81035d-40d3-4d38-8b49-7502b784c41a'
        URL = 'https://geolite.info/geoip/v2.1/city/'
        url = f'{URL}{ip_address}?license_key={maxmind_license_key}'

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()['city']
        else:
            return None

    def check_key(self, key):
        """Check if the API key is valid.

        Args:
            key (str): The API key.

        Returns:
            bool: True if the key is valid, False otherwise.

        """
        key = self.__storage.get('Auth', hashed_key=key)

        if not key:
            print("no key")
            return False

        if key.max_req <= key.used_req:
            print('max req')
            return False

        return True

    def save_response(self, request, response):
        """Save the API response.

        Args:
            request (Request): The request containing the API request details.
            response (Response): The response containing the API response.

        """
        key = self.__storage.get(
            'Auth', hashed_key=request.headers.get('X-APIEMPIR-KEY'))
        user = self.__storage.get('User', auth_id=key.id)
        req = Request(
            method=request.method,
            ip=request.remote_addr,
            status_code=response.status_code,
            path=request.path,
            date=datetime.now(),
            http_version=request.environ['SERVER_PROTOCOL'],
            user_id=user.id
        )
        self.__storage.new(req)
        self.__storage.save()

    def add_req(self, header):
        """Add a request to the API key.

        Args:
            header (str): The API key.

        """
        key = self.__storage.get('Auth', hashed_key=header)
        key.used_req += 1
        self.__storage.save()
