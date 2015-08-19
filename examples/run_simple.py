#!/usr/bin/env python
from speedrecorder import speedtest

def main():
    try:
        speedtest(quiet=False)
    except KeyboardInterrupt:
        print('Exiting.')

if __name__=='__main__':
    main()