========================
Cycle Calendar Generator
========================


.. image:: https://img.shields.io/pypi/v/cycle_calendar_generator.svg
        :target: https://pypi.python.org/pypi/cycle_calendar_generator
        :alt: PyPI Package Status

.. image:: https://img.shields.io/travis/ROldford/cycle_calendar_generator.svg
        :target: https://travis-ci.org/ROldford/cycle_calendar_generator
        :alt: Travis CI Status

.. image:: https://pyup.io/repos/github/ROldford/cycle_calendar_generator/shield.svg
     :target: https://pyup.io/repos/github/ROldford/cycle_calendar_generator/
     :alt: Updates

.. image:: https://readthedocs.org/projects/cycle-calendar-generator/badge/?version=latest
        :target: https://cycle-calendar-generator.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
        :target: https://www.python.org/)
        :alt: Compatible with Python 3.6+


*Generates iCal files for class schedules for schools using an N-day cycle*

If you're a teacher or a student, you probably have a 6 or 7-day cycle.
You'd like to enter your schedule into your calendar, but calendar software doesn't support "recur every n weekdays".
So you're out of luck, right? That's where Cycle Calendar Generator comes in.
You just need to make an Excel file with your school's schedule, and another Excel file for each teacher/student's schedule, and Cycle Calendar Generator does the rest.


* Documentation: https://cycle-calendar-generator.readthedocs.io.

Installation
------------

        ``$ pip install cycle_calendar_generator``

Usage
-----

1. Make a "Schedule Setup" Excel file
    a. Filename must be schedule_setup.xlsx
    b. Has 3 sheets, named "Period Timing", "Cycle Days List", and "Yearly Schedule"
    c. "Period Timing" sheet gives the period name/number, start time, and end time for each period
    d. "Cycle Days List" sheet lists the name/number of each day in the cycle
    e. "Yearly Schedule" sheet lists all dates in the school year and the matching day in the cycle
    f. Dates and times should be in the standard Excel date/time format
    g. All other data should be in text format, including numbers.
    h. See below for examples
2. Make an Excel file for each user that wants a schedule calendar
    a. The filename should match the user's name, and will be used to name the output calendar file. (Ex. Eric Idle's Excel file should be named "Eric Idle.xlsx", and  will generate "Eric Idle.ics")
    b. Has 1 sheet, named "User Schedule", that has the user's usual schedule for a cycle
    c. All data here should be in text format
    d. See below for examples
3. Put all files in any folder
4. Run the application as follows:

        ``$ cycle_calendar_generator path/to/schedule/files``

5. Schedule iCal files are found in the /output folder under the folder with your input Excel files.

.. _examples:

Examples
--------

**Period Timing**

+---------------+------------+----------+
| Period Number | Start Time | End Time |
+===============+============+==========+
| 1             | 8:00       | 9:00     |
+---------------+------------+----------+
| 2             | 9:00       | 10:00    |
+---------------+------------+----------+
| 3             | 10:00      | 11:00    |
+---------------+------------+----------+
| 4             | 11:00      | 12:00    |
+---------------+------------+----------+
| 5             | 12:00      | 13:00    |
+---------------+------------+----------+

*Times can be in either 24h or 12h format. "Period Number" should be text format, not number.*

**Cycle Days List**

+----+----+----+----+----+----+
| A1 | B2 | C3 | D4 | E5 | F6 |
+----+----+----+----+----+----+

*The entries here are the official names for all cycle days. Every cycle day entry in other sheets must match these values.*

**Yearly Schedule**

+---------+-----------+
| Date    | Cycle Day |
+---------+-----------+
| 8/31/18 | A1        |
+---------+-----------+
| 9/3/18  | B2        |
+---------+-----------+
| 9/4/18  | C3        |
+---------+-----------+
| 9/5/18  | D4        |
+---------+-----------+
| 9/6/18  | E5        |
+---------+-----------+
| 9/7/18  | F6        |
+---------+-----------+

*Dates can be displayed any way, but must be date format. Entries in the "Cycle Day" column must be an official cycle day as defined in Cycle Days List.*

**User Schedule**

+---------------+----------+----------+----------+---------+----------+----------+
| Period Number | A1       | B2       | C3       | D4      | E5       | F6       |
+---------------+----------+----------+----------+---------+----------+----------+
| 1             | Grade 8  |          | Grade 11 |         |          | Grade 8  |
+---------------+----------+----------+----------+---------+----------+----------+
| 2             |          | Grade 11 |          |         | Grade 8  |          |
+---------------+----------+----------+----------+---------+----------+----------+
| 3             | Lunch    | Lunch    | Lunch    | Lunch   | Lunch    | Lunch    |
+---------------+----------+----------+----------+---------+----------+----------+
| 4             | Grade 11 |          |          | Grade 8 |          | Grade 11 |
+---------------+----------+----------+----------+---------+----------+----------+
| 5             |          |          | Grade 8  |         | Grade 11 |          |
+---------------+----------+----------+----------+---------+----------+----------+

*"Period Number" should be text format, not number. The "Cycle Days" in the top row must be official cycle days as defined in Cycle Days List*

Tests
-----

For current Python version:
        ``python3 setup.py test``

For versions 3.5+
        ``tox``

It's recommended to use pyenv_ to install Python versions required by tox.
pyenv can be installed using Homebrew_::

        brew update
        brew install pyenv
        pyenv install 3.6.6 3.7.6

.. _pyenv: https://github.com/pyenv/pyenv
.. _Homebrew: https://brew.sh/

Contribute
----------

Contributions are always welcome! For thoughts on features or bug reports see Issues. If you're interested in contributing to this library, see details on doing so in the CONTRIBUTING.rst file in this repository.

Credits
-------

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elgertam/cookiecutter-pipenv`: https://github.com/elgertam/cookiecutter-pipenv
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Excel file reading was made possible by the openpyxl_ package, while iCal file reading and writing uses the ics_ package.

.. _openpyxl: https://bitbucket.org/openpyxl/openpyxl/src
.. _ics: https://github.com/C4ptainCrunch/ics.py

[ ~ Dependencies scanned by `PyUp.io <https://pyup.io/>`_ ~ ]

Licence
-------

* Free software: GNU General Public License v3
