from api.v1.views import app_apis
from flask import jsonify, request
import requests

def get_ip_location(ip_address):
    # Replace 'YOUR_MAXMIND_LICENSE_KEY' with your actual MaxMind license key
    maxmind_license_key = 'bb81035d-40d3-4d38-8b49-7502b784c41a'
    url = f'https://geolite.info/geoip/v2.1/city/\
        {ip_address}?license_key={maxmind_license_key}'
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['city']
    else:
        return None


@app_apis.route('/weather/<function>', methods=['GET'], strict_slashes=False)
@app_apis.route('/weather', methods=['GET'], strict_slashes=False)
def get_endpoints(function=None):
    """ Get all endpoints """
    weather_api_key = '807fc75c10194ef1a6c223212241403'
    url = 'http://api.weatherapi.com/v1/'
    weather_functions = ['current', 'forecast',
                         'search', 'history']
    if not function:
        return jsonify({"Error": "No function provided"}), 400
    if function not in weather_functions:
        return jsonify({"Error": "Function not found"}), 404
    if function == 'search':
        ip = get_ip_location(request.remote_addr)
        api_url = f'{url}{function}.json?key={weather_api_key}&q={ip}'
        response = requests.get(api_url)
    else:
        api_url = f'{url}{function}.json?key={weather_api_key}&\
            {request.query_string.decode()}'
        response = requests.get(api_url)
    return response.json(), response.status_code


@app_apis.route('/currency', methods=['GET'], strict_slashes=False)
def currency():
    """ Get currency """
    key = 'access_key=m4UqvZZH7GW4UFoW'
    api_url = f'https://api.exchangeratesapi.net/v1/exchange-rates/latest?{key}'
    api_url += f'&base={request.args["base"]}'
    answer = requests.get(api_url)
    return answer.json(), answer.status_code
