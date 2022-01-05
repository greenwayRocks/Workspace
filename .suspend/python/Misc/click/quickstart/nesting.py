import click


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.secho('Initialized the database', fg='green', bold=True)


@cli.command()
def dropdb():
    click.secho('Dropped the database', fg='red', bold=True)


if __name__ == '__main__':
    cli()
