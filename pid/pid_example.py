#!/usr/bin/env python

"""Prints the process id and process parent id"""

import os
import time


print "PID: %s" % os.getpid()
print "PPID: %s" % os.getppid()
print "An oportunity to see the process status in the terminal"
print "\t$ ps -fp %s" % os.getpid()
time.sleep(10)