import click

@click.command()
@click.argument('zipcode')
def main(zipcode):
    click.echo("The weather in {} is super fly!".format(zipcode))

if __name__ == "__main__":
    main()