# -*- coding: utf-8 -*-

"""Main module."""
import argparse
import os
# from os import os.getcwd
# from os import os.scandir
# from os import path

import openpyxl

SCHEDULE_SETUP_FILENAME = 'schedule_setup.xlsx'

ERROR_MISSING_SETUP_FILE = 'No schedule setup file found'
ERROR_INVALID_FOLDER = 'Not a valid folder'
ERROR_INVALID_SETUP_FILE = 'Setup file does not follow proper format'
ERROR_SETUP_FILE_NOT_EXCEL = 'Setup file is not a readable Excel file'

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
    return_value = os.getcwd()
  else:
    return_value = parsed_args.folder
  return return_value

def readScheduleSetupFile(folder):
  return_value = None
  if (os.path.isdir(folder)):
    schedule_setup_filepath = "{}/{}".format(folder, SCHEDULE_SETUP_FILENAME)
    scanned_files = []
    try:
      return_value = openpyxl.load_workbook(schedule_setup_filepath)
    except Exception as e:
      exception_type = str(type(e))
      for case in switch(exception_type):
        if case("<class 'zipfile.BadZipFile'>"):
          raise ValueError(ERROR_SETUP_FILE_NOT_EXCEL)
          break
        if case("<class 'FileNotFoundError'>"):
          raise ValueError(ERROR_MISSING_SETUP_FILE)
        if case:
          raise e
  else:
    raise ValueError(ERROR_INVALID_FOLDER)
  return return_value

def parseScheduleSetup(workbook):
  return_value = SetupData()
  try:
    ws_periodTiming = workbook['Period Timing']
    ws_cycleDaysList = workbook['Cycle Days List']
    ws_yearlySchedule = workbook['Yearly Schedule']
  except Exception as e:
    exception_type = str(type(e))
    for case in switch(exception_type):
      if case("<class 'KeyError'>"):
        raise ValueError(ERROR_INVALID_SETUP_FILE)
        break
      if case():
        raise e
  return return_value

class SetupData:
  def __init__(self):
    self.periodTiming = {}
    self.cycleDaysList = []
    self.yearlySchedule = {}

  def appendPeriod(self, periodNumber, startTime, endTime):
    pass

  def appendCycleDay(self, cycleDay):
    pass

  def appendScheduleDay(self, date, cycleDay):
    pass

class switch(object):
  def __init__(self, value):
    self.value = value
    self.fall = False

  def __iter__(self):
    """Return the match method once, then stop"""
    yield self.match
    raise StopIteration

  def match(self, *args):
    """Indicate whether or not to enter a case suite"""
    if self.fall or not args:
      return True
    elif self.value in args:
      self.fall = True
      return True
    else:
      return False
