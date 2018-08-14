#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cycle_calendar_generator` package."""


import unittest
from unittest import mock

from cycle_calendar_generator import cycle_calendar_generator


class Test_get_args(unittest.TestCase):
    """Tests for `cycle_calendar_generator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    @mock.patch('cycle_calendar_generator.cycle_calendar_generator.argparse.ArgumentParser.parse_args')
    def test_if_arg_is_string(self, mock_parse_args):
        """Normal input on command line"""
        mock_parse_args.return_value = cycle_calendar_generator.argparse.Namespace(directory='string')
        self.assertIsInstance(cycle_calendar_generator.getArgs(), str)

    @mock.patch('cycle_calendar_generator.cycle_calendar_generator.argparse.ArgumentParser.parse_args')
    def test_if_arg_is_not_string(self, mock_parse_args):
        """Abnormal command line input"""
        mock_parse_args.return_value = cycle_calendar_generator.argparse.Namespace(directory=42)
        self.assertRaises(SyntaxError, cycle_calendar_generator.getArgs)

    # @mock.patch('cycle_calendar_generator.argparse.parse_args')
    # @mock.patch('cycle_calendar_generator.argparse.parse_args')
    # def test_gets_current_dir_if_no_arg_given(self):
    #     """Test something."""
        # mock_parse_args.return_value = argparse.Namespace(directory=None)
        # self.assertRaises(SyntaxError, cycle_calendar_generator.getArgs)



# Get directory from args
# Check for schedule setup Excel file
# Open and parse schedule setup file (checking for valid data)
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
