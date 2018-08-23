#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cycle_calendar_generator` package."""


import unittest
from unittest import mock
import os

from pyfakefs import fake_filesystem_unittest

from cycle_calendar_generator import cycle_calendar_generator


class Test_get_args(unittest.TestCase):
    # Get directory from args
    """Tests function to get folder argument and give default if none given"""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @mock.patch(
        'cycle_calendar_generator.cycle_calendar_generator.argparse.ArgumentParser.parse_args'
    )
    def test_if_arg_is_string(self, mock_parse_args):
        """Normal input on command line"""
        mock_parse_args.return_value = cycle_calendar_generator.argparse.Namespace(
            folder='string'
        )
        self.assertIsInstance(cycle_calendar_generator.getArgs(), str)

    @mock.patch(
        'cycle_calendar_generator.cycle_calendar_generator.argparse.ArgumentParser.parse_args'
    )
    @mock.patch('cycle_calendar_generator.cycle_calendar_generator.getcwd')
    def test_gets_current_dir_if_no_arg_given(self, mock_getcwd, mock_parse_args):
        """Use current working directory if no folder given"""
        cwd_string = 'current working directory'
        mock_parse_args.return_value = cycle_calendar_generator.argparse.Namespace(
            folder=None
        )
        mock_getcwd.return_value = cwd_string
        self.assertEqual(cycle_calendar_generator.getArgs(), cwd_string)

class Test_parse_schedule_setup_file(fake_filesystem_unittest.TestCase):
    # Check for schedule setup Excel file
    # Open and parse schedule setup file (checking for valid data)
    # Parsing should generate:
    ## [dict]periodTiming -> [int]periodNumber: [tuple(Date, Date)](startTime, endTime)
    ## [list]CycleDaysList -> (str)cycleDay {showing all cycleDay strings}
    ## [dict]yearlySchedule -> [Date]date: [str]cycleDay
    """Tests function to open and parse schedule setup Excel file"""

    good_folder_path = ''
    bad_folder_path = ''
    not_a_folder_path = ''
    bad_folder_filename_list = ['TeacherOne.xlsx', 'TeacherTwo.xlsx']
    good_folder_filename_list = (
      bad_folder_filename_list
      + [cycle_calendar_generator.SCHEDULE_SETUP_FILENAME]
    )
    bad_folder_full_filepath_list = []
    good_folder_full_filepath_list = []

    def setUp(self):
      self.setUpPyfakefs()
      # set up variables
      self.good_folder_path = '/test-good'
      self.bad_folder_path = '/test-bad'
      self.not_a_folder_path = '/test-notafolder'
      # Make file paths in fakefs
      os.mkdir(self.good_folder_path)
      os.mkdir(self.bad_folder_path)
      # Add files in fakefs

      for file in self.bad_folder_filename_list:
        bad_folder_filepath = "{}/{}".format(self.bad_folder_path, file)
        self.bad_folder_full_filepath_list.append(bad_folder_filepath)
        open(bad_folder_filepath, 'a').close()

      for file in self.good_folder_filename_list:
        good_folder_filepath = "{}/{}".format(self.good_folder_path, file)
        self.good_folder_full_filepath_list.append(good_folder_filepath)
        open(good_folder_filepath, 'a').close()

    def test_opens_and_parses_correct_file(self):
        """Expected behavior: finds file with preset filename, opens and parses,
        returning object containing setup dicts and lists"""
        pass

    def test_raises_exception_if_invalid_path(self):
        """If input string is not a valid folder path, throw ValueError"""
        # create an invalid folder path
        # pass into parseScheduleSetup and check for error raised
        self.assertRaisesRegex(
            ValueError,
            'Not a valid folder', # TODO: use string constant from code
            cycle_calendar_generator.parseScheduleSetup,
            self.not_a_folder_path
        )

    def test_raises_exception_if_no_setup_file(self):
        """If no Excel file matching preset filename exists, throw ValueError"""
        self.assertRaisesRegex(
            ValueError,
            'No schedule setup file found', # TODO: use string constant from code
            cycle_calendar_generator.parseScheduleSetup,
            self.bad_folder_path
        )







# Parsing should generate:
## [dict]periodTiming -> [int]periodNumber: [tuple(Date, Date)](startTime, endTime)
## [list]CycleDaysList -> (str)cycleDay {showing all cycleDay strings}
## [dict]yearlySchedule -> [Date]date: [str]cycleDay
# Check for teacher schedule Excel files
# Iterate over teacher schedule files; for each...
## Create new iCal Calendar object
## Open teacher schedule file
## Check if file is valid Excel file (exception check)
## Check that file's periodNumbers (in first column) match those in setup file
## Check that file's cycleDays (in first row) match those in setup file
## Iterate over cycleDay columns, generating list of objects; for each...
### Generate dailySchedule object, 2 properties:
#### [str]cycleDay
#### [dict]schedule -> [int]periodNumber: [str]className
### Sort list by cycleDay property
## Iterate over date:cycleDay dict, for each...
### Find dailySchedule object matching cycleDay
### Iterate over periodNumbers, for each...
#### Check if className exists for this periodNumber, skip this if not
#### Generate iCal Event object
##### Name of event = className
##### Start date, end date = this date
##### Start time, end time = found by referencing periodTiming
#### Append Event object to Calendar
## Save Calendar, using filename from teacher schedule file
