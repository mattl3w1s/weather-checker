import click
import os
from dotenv import load_dotenv
import requests

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

def create_url_from_city_name(city_name):
    return ''

def get_weather_from_city_name(city_name):
    url = create_url_from_city_name(city_name)
    weather_request = requests.get(url)
    return weather_request.json()

@click.command()
@click.argument('city_name')
def main(city_name):
    weather = get_weather_from_city_name(city_name)
    click.echo("The weather in {} is {}".format(city_name, weather))

if __name__ == "__main__":
    main()