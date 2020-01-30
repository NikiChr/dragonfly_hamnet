#!/usr/bin/python
# -*- coding: utf-8 -*-
# test.py

from progress.bar import Bar, IncrementalBar
from progress.spinner import Spinner
import time
import settings as set


spinner = Spinner('Restarting stopped hosts ')
while True:
    time.sleep(5)
    set.restartExited()
    spinner.next()
