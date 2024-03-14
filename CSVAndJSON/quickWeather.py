#! python3
import json
import requests
import sys
from APIKEY import openweathermap_KEY

# Get location from command line arguments
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()

location = ' '.join(sys.argv[1:])
api_key = openweathermap_KEY

# Geocoding....
geocode_url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}'
response = requests.get(geocode_url)
response.raise_for_status()

# Parse lat and lon
geocode_data = json.loads(response.text)
if not geocode_data:
    print("Location not found")
    sys.exit()

lat = geocode_data[0]['lat']
lon = geocode_data[0]['lon']


# Download JSON data from openweathermap. org's API.
url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt=3&appid={api_key}&units=metric'
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a python variable
weatherData = json.loads(response.text)

# Print weather descriptions

w = weatherData['list']
print(f"Current weather in {location}")
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'], '-', f"Temp: {w[0]['main']['temp']}°C")
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'], '-', f"Temp: {w[1]['main']['temp']}°C")
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'], '-', f"Temp: {w[2]['main']['temp']}°C")

# city = input("Enter City:")

# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# res = requests.get(url)
# data = res.json()

# humidity = data['main']['humidity']
# pressure = data['main']['pressure']
# wind = data['wind']['speed']
# description = data['weather'][0]['description']
# temp = data['main']['temp']

# print('Temperature:',temp,'°C')
# print('Wind:',wind)
# print('Pressure: ',pressure)
# print('Humidity: ',humidity)
# print('Description:',description)