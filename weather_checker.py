import click
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

def create_url_from_city_name(city_name):
    city_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,OPEN_WEATHER_API_KEY)
    return city_url

def get_weather_from_city_name(city_name):
    try:
        url = create_url_from_city_name(city_name)
        weather_request = requests.get(url)
        return weather_request.json()
    except:
        print("Access to OpenWeather currently unavailable")
        quit()

def get_pretty_weather(weather):
    try:
        city = weather['name']
    except:
        print("Invalid City")
        quit()
    temperature = (weather['main']['temp']-273.15)*(9/5)+32
    weather_conditions = weather['weather'][0]['description']
    pretty_weather = {'City':city,'Temperature':temperature,'Weather_Conditions':weather_conditions}
    return pretty_weather

@click.command()
@click.argument('city_name')
def main(city_name):
    weather = get_weather_from_city_name(city_name)
    pweather = get_pretty_weather(weather)
    pprint(pweather)

if __name__ == "__main__":
    main()
