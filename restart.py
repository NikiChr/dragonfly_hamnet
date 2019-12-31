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



#set.measureTime('golang',True,'201910181448','201910182258',2,53)

#print ("%s ist %s sehr %s" % ('Das %s Feature','wirklich','cool')
