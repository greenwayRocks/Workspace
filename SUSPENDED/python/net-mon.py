import os
import subprocess
import sys
from decouple import config

IP_NETWORK = config('IP_NETWORK')

proc = subprocess.Popen(['ping', '-c 5', IP_NETWORK], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    connected_ip = line.decode('utf-8').split()[3]
    if IP_NETWORK in connected_ip:
        subprocess.Popen(['espeak', 'INTRUSION'])

    # if connected_ip == IP_DEVICE:
    #     subprocess.Popen(['say', 'Connected To the Internet!'])
