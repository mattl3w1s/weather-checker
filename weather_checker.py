import click

@click.command()
@click.argument('city_name')
def main(city_name):
    click.echo("The weather in {} is super fly!".format(city_name))

if __name__ == "__main__":
    main()