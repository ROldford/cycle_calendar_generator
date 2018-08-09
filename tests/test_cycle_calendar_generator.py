#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cycle_calendar_generator` package."""


import unittest

from cycle_calendar_generator import cycle_calendar_generator


class TestCycle_calendar_generator(unittest.TestCase):
    """Tests for `cycle_calendar_generator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""


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
