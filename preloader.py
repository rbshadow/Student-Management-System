import os
import platform
import sys
import time


operating_system = platform.system()


def load(string):
    string = string
    dot_dot = '...'

    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')

    print('\n\n\n\n\n\n')
    print(string, end='')
    for char in dot_dot:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.15)
    print()
