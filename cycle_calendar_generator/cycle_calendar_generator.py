# -*- coding: utf-8 -*-

"""Main module."""
import argparse
from os import getcwd

def getArgs():
    return_value = ''
    parser = argparse.ArgumentParser(description='Input folder')
    parser.add_argument('folder', nargs='?', action='store', help='folder with input Excel files')
    parsed_args = parser.parse_args()
    return_value = parsed_args.folder
    return return_value
