#!/usr/bin/env python3
from network import *

import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

def main():
    # Check disk usage and cpu usage
    if not check_disk_usage('/') or not check_cpu_usage():
        print('ERROR!')
    else:
        print('Everything is OK')

    # Check network connectivity
    if check_localhost() and check_connectivity():
        print('Network connection, GOOD!')
    else:
        print('NEW ERROR!')


if __name__ == '__main__':
    main()
