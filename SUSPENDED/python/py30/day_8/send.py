import sys
import requests
from formatting import format_msg

def send(name, website=None, verbose=False):
    if website:
        msg = format_msg(name, website)
    else:
        msg = format_msg(name)

    if verbose:
        print(name, website)

    res = requests.get('https://httpbin.org/json')
    if res.status_code == 200:
        return res.json()
    else:
        return 'There was an error' + str(res.status_code)

if __name__ == '__main__':
    name = 'Unknown'
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, verbose=True)
    print(response)
