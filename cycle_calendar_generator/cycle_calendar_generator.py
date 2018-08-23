# -*- coding: utf-8 -*-

"""Main module."""
import argparse
from os import getcwd
from os import scandir
from os import path

SCHEDULE_SETUP_FILENAME = 'schedule_setup.xslx'

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
  if (path.isdir(folder)):
    # try to find and open SCHEDULE_SETUP_FILENAME
    # if it doesn't exist, raise ValueError
    schedule_setup_filepath = "{}/{}".format(folder, SCHEDULE_SETUP_FILENAME)
    scanned_files = []
    try:
      with scandir(schedule_setup_filepath) as scanner:
        for entry in scanner:
          if entry.is_file:
            scanned_files.append(entry.name)
    except FileNotFoundError:
      raise ValueError('No schedule setup file found')
    if (SCHEDULE_SETUP_FILENAME in scanned_files):
      # open file and try parse
      return_value = 'is a real file'
    else:
      raise ValueError('No schedule setup file found')
      # TODO: string constant
  else:
    raise ValueError('Not a valid folder')
    # TODO: string constant
  return return_value
