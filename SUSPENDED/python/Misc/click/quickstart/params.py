import click


@click.command()
@click.option('--count', '-c', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.secho(f'Hello {name}', fg='white', bg='black', bold=True)


if __name__ == '__main__':
    hello()
