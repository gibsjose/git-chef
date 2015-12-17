#!/usr/bin/env python3

#   git-chef
#
#   16 Dec 2015
#
#   Joe Gibson (gibsjosej@gmail.com)
#
#   License: MIT (https://gibsjose.mit-license.org)
#
#   https://gibsjose.com

from enum import Enum
import sys
import os
import traceback
import argparse
import re
import operator
import time

def main():
    global args

    # Perform manual indexing
    if args.query == 'index':
        print('indexing')

    # Parse description
    else:
        print('searching for \'' + args.query + '\'')

if __name__ == '__main__':
    try:
        start_time = time.time()

        parser = argparse.ArgumentParser(prog='git-chef', description='search for the right git command, right from the command line')

        # Options
        parser.add_argument('-v', '--verbose', action='store_true', default=False, help='verbose mode')

        # Arguments
        parser.add_argument('query')

        # Commands
        # subparsers = parser.add_subparsers(help='commands:', dest='command')
        # index_parser = subparsers.add_parser('index', help='index cookbooks and recipes')

        args = parser.parse_args()

        main()
        if args.verbose: print('\n' + time.asctime())
        if args.verbose: print('Total Runtime: ', end='')
        if args.verbose: print(str((time.time() - start_time) * 1000) + ' ms')
        sys.exit(0)
    except KeyboardInterrupt as e: # Ctrl-C
        raise e
    except SystemExit as e: # sys.exit()
        raise e
    except Exception as e:
        print('Error: Unexpected Exception')
        print(str(e))
        traceback.print_exc()
        os._exit(1)
