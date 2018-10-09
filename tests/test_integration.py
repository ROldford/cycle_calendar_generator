#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Integration test for `cycle_calendar_generator` package."""

import unittest
import os
import sys

CURRENT_WORKING_DIRECTORY = os.path.dirname(os.path.realpath(sys.argv[0]))
# TODO: Fix all paths to use path.join without hardcoded folder separators
INTEGRATION_TEST_FOLDER = os.path.join(
  CURRENT_WORKING_DIRECTORY,
  '/tests/integration_test'
)
TEST_FILES_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, '/testing_files')
TEST_EXPECTED_OUTPUT_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, '/expected')
TEST_TEMP_FOLDER = os.path.join(INTEGRATION_TEST_FOLDER, '/temp')
TEST_OUTPUT_FOLDER = os.path.join(TEST_TEMP_FOLDER, '/output')

class Test_integration(unittest.TestCase):
  """Tests function to get folder argument and give default if none given"""

  def setUp(self):
    # copy test input files from TEST_FILES_FOLDER to TEST_TEMP_FOLDER
    pass

  def tearDown(self):
    # delete all files and folders in TEST_TEMP_FOLDER
    pass

  def test_script_works_in_normal_case(self):
    # run script
    # read output icals into dictionary (teacher name as key)
    # read expected output icals into similar dictionary
    # assert both dicts have same size
    # assert each key in output has matching in expected
    # assert values from matching keys are the same
    pass
