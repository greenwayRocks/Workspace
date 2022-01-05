import click


@click.group()
@click.option('--verbose', '-v', is_flag=True)
def cli(verbose):
    if verbose:
        click.echo('We are in verbose mode')


@cli.command()
@click.option('--string', default='World', help='string to print')
@click.option('--repeat', default=1, help='no of times to greet')
@click.argument('out', type=click.File('w'), default='-', required=False)
def say(string, repeat, out):
    '''This script greets you'''
    for x in range(repeat):
        click.echo('Hello %s!' % string, file=out)
