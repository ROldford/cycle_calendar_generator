#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Integration test for `cycle_calendar_generator` package."""

import unittest
import os
import sys
import shutil
import subprocess
from pathlib import Path

import ics

CURRENT_WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
# TODO: Fix all paths to use path.join without hardcoded folder separators
INTEGRATION_TEST_FOLDER = os.path.join(
  CURRENT_WORKING_DIRECTORY,
  'integration_test'
)
TEST_FILES_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, 'testing_files')
TEST_EXPECTED_OUTPUT_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, 'expected')
TEST_TEMP_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, 'temp')
TEST_OUTPUT_FOLDER = os.path.join(TEST_TEMP_FOLDER, 'output')
SCRIPT_PATH = os.path.join(
  Path(CURRENT_WORKING_DIRECTORY).parent,
  'cycle_calendar_generator/cycle_calendar_generator.py'
)

class Test_integration(unittest.TestCase):
  """Tests function to get folder argument and give default if none given"""

  @classmethod
  def setUpClass(cls):
    if (not os.path.exists(TEST_EXPECTED_OUTPUT_FOLDER)):
      os.mkdir(TEST_EXPECTED_OUTPUT_FOLDER)
    if (not os.path.exists(TEST_TEMP_FOLDER)):
      os.mkdir(TEST_TEMP_FOLDER)

  def setUp(self):
    # copy test input files from TEST_FILES_FOLDER to TEST_TEMP_FOLDER
    with os.scandir(TEST_FILES_FOLDER) as testing_files:
      for file in testing_files:
        source_path = file.path
        dest_path = os.path.join(TEST_TEMP_FOLDER, file.name)
        shutil.copy(source_path, dest_path)

  def tearDown(self):
    # delete all files and folders in TEST_TEMP_FOLDER
    with os.scandir(TEST_TEMP_FOLDER) as files_to_delete:
      for file in files_to_delete:
        if file.is_dir():
          shutil.rmtree(file.path)
        else:
          os.remove(file.path)

  def test_script_works_in_normal_case(self):
    # run script
    subprocess.run(['python3', SCRIPT_PATH, TEST_TEMP_FOLDER])
    # read output icals into dictionary (teacher name as key)
    output_files = {}
    with os.scandir(TEST_OUTPUT_FOLDER) as output_files_scan:
      for file in output_files_scan:
        if file.is_file():
          path, filename = os.path.split(file.path)
          teacher_name = os.path.splitext(filename)[0]
          with open(file.path) as ical:
            calendar = ics.Calendar(ical.read())
          sorted_events = sorted(calendar.events, key=lambda event:event.begin)
          output_files[teacher_name] = sorted_events
    # read expected output icals into similar dictionary
    expected_files = {}
    with os.scandir(TEST_EXPECTED_OUTPUT_FOLDER) as expected_files_scan:
      for file in expected_files_scan:
        if file.is_file():
          path, filename = os.path.split(file.path)
          teacher_name = os.path.splitext(filename)[0]
          with open(file.path) as ical:
            calendar = ics.Calendar(ical.read())
          sorted_events = sorted(calendar.events, key=lambda event:event.begin)
          expected_files[teacher_name] = sorted_events
    # assert both dicts have same size
    self.assertEqual(len(output_files), len(expected_files))
    # assert each key in output has matching in expected
    for key in output_files.keys():
      self.assertTrue(key in expected_files)
      # assert values from matching keys are the same
      output_events = output_files[key]
      expected_events = expected_files[key]
      for i in range(len(output_events)):
        output_event = output_events[i]
        expected_event = expected_events[i]
        self.assertEqual(output_event.name, expected_event.name)
        self.assertEqual(
          output_event.begin.to('utc'),
          expected_event.begin.to('utc')
        )
        self.assertEqual(
          output_event.end.to('utc'),
          expected_event.end.to('utc')
        )
