# -*- coding: utf-8 -*-

"""Main module."""
import argparse
from os import getcwd
from os import path

def getArgs():
    return_value = None
    parser = argparse.ArgumentParser(description='Input folder')
    parser.add_argument(
        'folder',
        nargs='?',
        action='store',
        help='folder with input Excel files'
    )
    parsed_args = parser.parse_args()
    if parsed_args.folder == None:
        return_value = getcwd()
    else:
        return_value = parsed_args.folder
    return return_value

def parseScheduleSetup(folder):
    return_value = None
    if (path.islink(folder)):
        return_value = '?'
    else:
        raise ValueError('Not a valid folder')
    return return_value
