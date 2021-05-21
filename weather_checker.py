import click
import os
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

@click.command()
@click.argument('city_name')
def main(city_name):
    click.echo("The weather in {} is super fly!".format(city_name))

if __name__ == "__main__":
    main()