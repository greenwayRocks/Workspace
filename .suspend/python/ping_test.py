# Create a Network ping scanner utility

import platform
from subprocess import Popen, PIPE
import argparse

parser = argparse.ArgumentParser(description='Ping Scanner utility')

parser.add_argument('--network', '-n', help='Network segment', dest='network', required=True)
parser.add_argument('--host', '-m', help='Host segment', dest='host', required=True)

args = parser.parse_args()

for ip in range(1, int(args.host) + 1):
    ipAddr = args.network + '.'  + str(ip)
    print(f'Scanning IP Address {ipAddr} ...')

    if platform.system() == 'Linux':
        proc = Popen(['ping', '-c', '3', ipAddr], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    elif platform.system() == 'Windows':
        proc = Popen(['ping', ipAddr], stdin=PIPE, stdout=PIPE, stderr=PIPE)

stdout, stderr = proc.communicate(input=None)
stdout = stdout.decode('utf-8')

print(stdout)

if "bytes from" in stdout or "Reply from" in stdout:
    print('The machine replied with an ECHO ICMP request!')
