# -*- coding: utf-8 -*-

"""Main module."""
import argparse
import os
import openpyxl

SCHEDULE_SETUP_FILENAME = 'schedule_setup.xlsx'

ERROR_MISSING_SETUP_FILE = 'No schedule setup file found'
ERROR_INVALID_FOLDER = 'Not a valid folder'
ERROR_INVALID_SETUP_FILE = 'Setup file does not follow proper format'
ERROR_SETUP_FILE_NOT_EXCEL = 'Setup file is not a readable Excel file'
ERROR_INVALID_SCHEDULE_FILE = 'Schedule file is not a readable Excel file'

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
    rows_periodTiming = tuple(ws_periodTiming.rows)
    rows_periodTiming = rows_periodTiming[1:]
    for row in rows_periodTiming:
      return_value.appendPeriod(row[0].value, row[1].value, row[2].value)
    list_cycleDaysList = []
    for row in ws_cycleDaysList.iter_rows(
      max_row=1, max_col=ws_cycleDaysList.max_column
    ):
      for cell in row:
        list_cycleDaysList.append(cell.value)
    return_value.setCycleDays(list_cycleDaysList)
    rows_yearlySchedule = tuple(ws_yearlySchedule.rows)
    rows_yearlySchedule = rows_yearlySchedule[1:]
    for row in rows_yearlySchedule:
      return_value.appendScheduleDay(row[0].value, row[1].value)
  except Exception as e:
    exception_type = str(type(e))
    for case in switch(exception_type):
      if case("<class 'KeyError'>"):
        raise ValueError(ERROR_INVALID_SETUP_FILE)
        break
      if case():
        raise e
  return return_value

def readTeacherScheduleFile(filepath):
  return_value = None
  try:
    return_value = openpyxl.load_workbook(filepath)
  except Exception as e:
    exception_type = str(type(e))
    for case in switch(exception_type):
      if case("<class 'zipfile.BadZipFile'>"):
        raise ValueError(ERROR_INVALID_SCHEDULE_FILE)
        break
      if case("<class 'FileNotFoundError'>"):
        raise ValueError(ERROR_INVALID_SCHEDULE_FILE)
      if case:
        raise e
  return return_value

def parseTeacherSchedule(workbook, setupData):
  return_value = ScheduleData(setupData.periodList)
  try:
    ws_teacherSchedule = workbook['Teacher Schedule']
    cols_teacherSchedule = tuple(ws_teacherSchedule.columns)
    # get period numbers
    schedule_periodNumberCol = cols_teacherSchedule[0]
    schedule_periodNumberCol = schedule_periodNumberCol[1:]
    setup_periodList = setupData.periodList
    for cell in schedule_periodNumberCol:
      if not (cell.value in setup_periodList):
        raise ValueError(ERROR_INVALID_SCHEDULE_FILE)
    # cycle through columns and add schedule days
    schedule_dayCols = cols_teacherSchedule[1:]
    for day in schedule_dayCols:
      day_list = list(day)
      return_value.addScheduleDay(day_list)
  except Exception as e:
    exception_type = str(type(e))
    for case in switch(exception_type):
      if case("<class 'KeyError'>"):
        raise ValueError(ERROR_INVALID_SCHEDULE_FILE)
      if case():
        raise e
  return return_value

# Convenience objects/functions
class SetupData:
  def __init__(self):
    self.periodList = []
    self.periodTiming = {}
    self.cycleDaysList = []
    self.yearlySchedule = {}

  def appendPeriod(self, periodNumber, startTime, endTime):
    if periodNumber not in self.periodTiming:
      self.periodTiming[periodNumber] = (startTime, endTime)
      self.periodList.append(periodNumber)
    else:
      raise ValueError(ERROR_INVALID_SETUP_FILE)

  def setCycleDays(self, cycleDays):
    self.cycleDaysList.clear()
    self.cycleDaysList = cycleDays

  def appendScheduleDay(self, date, cycleDay):
    if date not in self.yearlySchedule:
      self.yearlySchedule[date] = cycleDay
    else:
      raise ValueError(ERROR_INVALID_SETUP_FILE)

class ScheduleData:
  def __init__(self, periodList):
    self.teacherSchedule = {}
    self.periodList = periodList

  def addScheduleDay(self, schedule_list):
    schedule_day_key = schedule_list[0]
    schedule_periods_list = schedule_list[1:]
    if len(schedule_periods_list) != len(self.periodList):
      raise ValueError(ERROR_INVALID_SCHEDULE_FILE)
    schedule_day = dict(zip(self.periodList, schedule_periods_list))
    self.teacherSchedule[schedule_day_key] = schedule_day

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
