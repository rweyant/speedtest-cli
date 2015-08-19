#!/usr/bin/env python
print(1)
from speedrecorder import speedtest
from time import sleep
from argparse import ArgumentParser as ArgParser
print(2)
description = ('Run speedrecorder continuously.')
print(3)
wrapper_parser = ArgParser(description=description)
print(4)
wrapper_parser.add_argument('--delay', dest='delay', default=15,type=int,
                    help='Number of minutes to wait in between runs')
print(5)
args = wrapper_parser.parse_args()
print(6)
print(args.delay)
while True:    
    speedtest()
    sleep(60*args.delay)

