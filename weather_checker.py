import click
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

def city_or_zip(location):
    city = True
    if type(location) == 'int':
        city = False
    return city

def create_url_from_city_name(city_name):
    city_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,OPEN_WEATHER_API_KEY)
    return city_url

def create_url_from_zip_code(zip):
    city_url = "https://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}".format(zip,OPEN_WEATHER_API_KEY)
    return city_url

def get_weather_from_city_name(city_name):
    try:
        url = create_url_from_city_name(city_name)
        weather_request = requests.get(url)
        return weather_request.json()
    except:
        print(" ERROR: Access to OpenWeather currently unavailable")
        quit()

def get_weather_from_zip_code(zip):
    try:
        url = create_url_from_zip_code(zip)
        weather_request = requests.get(url)
        return weather_request.json()
    except:
        print(" ERROR: Access to OpenWeather currently unavailable")
        quit()

def get_pretty_weather(weather):
    try:
        city = weather['name']
    except:
        print(" ERROR: Invalid Location")
        quit()
    temperature = (weather['main']['temp']-273.15)*(9/5)+32
    weather_conditions = weather['weather'][0]['description']
    pretty_weather = {'City':city,'Temperature':temperature,'Weather_Conditions':weather_conditions}
    return pretty_weather

@click.command()
@click.argument('location')
def main(location):
    city = city_or_zip(location)
    if city:
        weather = get_weather_from_city_name(location)
    else:
        weather = get_weather_from_zip_code(location)
    pweather = get_pretty_weather(weather)
    pprint(pweather)

if __name__ == "__main__":
    main()
