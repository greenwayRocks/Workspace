#!/usr/bin/env python3

import click
import requests
import os


class Weather:
    def __init__(self, location, api_key):
        self.location = location
        self.api_key = api_key

    def get_weather(self):
        url = 'http://api.openweathermap.org/data/2.5/weather'

        query = {
            'q': self.location,
            'appid': self.api_key
        }

        res = requests.get(url, params=query)
        return res.json()['weather'][0]['description']

    def __str__(self):
        return 'My Weather API App Instance, location: {}'.format(self.location)


@click.group()
def main():
    pass


@main.command()
@click.argument('location')
@click.option('--api-key', '-a', envvar='API_KEY', help='your API key for OpenWeatherMap API')
def current(location, api_key):
    '''My little weather tool.'''
    weather = Weather(location, api_key)
    click.secho('{}'.format(weather), fg='white', bg='blue')
    print(f'The weather in {location} right now: {weather.get_weather()}')


@main.command()
@click.option('--api-key', '-a', prompt='[] Please enter your API key', help='your API key for OpenWeatherMap API')
def config(api_key):
    '''Stores configuration values in a file.'''
    config_file = os.path.expanduser('~/.weather.cfg')

    with open(config_file, 'w') as cfg:
        cfg.write(api_key)


if __name__ == '__main__':
    main()
