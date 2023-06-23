import requests
import json
from termcolor import colored

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(response.text)
    return ip_data['ip']

def get_location_info():
    ip = get_public_ip()
    response = requests.get(f'http://ip-api.com/json/{ip}')
    location_data = json.loads(response.text)
    return location_data

def get_internet_service_provider():
    location_data = get_location_info()
    return location_data['isp']

def print_stylish(text):
    print(colored(text, 'cyan', attrs=['bold', 'underline']))

def main():
    isp = get_internet_service_provider()
    ip = get_public_ip()
    location_data = get_location_info()
    latitude = location_data['lat']
    longitude = location_data['lon']

    print_stylish('Internet Service Provider:')
    print(isp)
    print_stylish('Public IP Address:')
    print(ip)
    print_stylish('Geographic Location:')
    print(f'Latitude: {latitude}, Longitude: {longitude}')

if __name__ == '__main__':
    main()
