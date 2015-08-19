#!/usr/bin/env python

from speedrecorder import speedtest
from time import sleep
from argparse import ArgumentParser as ArgParser

description = ('Run speedrecorder continuously.')

wrapper_parser = ArgParser(description=description)

wrapper_parser.add_argument('--delay', dest='delay', default=15,type=int,
                    help='Number of minutes to wait in between runs')

args = wrapper_parser.parse_args()

try:
    while True:    
        speedtest()
        sleep(60*args.delay)
except KeyboardInterrupt:
    print("Exiting.")
