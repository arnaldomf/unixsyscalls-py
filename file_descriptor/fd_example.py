#!/usr/bin/env python

import os
import sys
import traceback

# open returns a File object
passwd = open('/etc/passwd')
hosts = open('/etc/hosts')
# print file descriptors
print "PASSWD FD: %s" % passwd.fileno()
print "HOSTS FD: %s" % hosts.fileno()
# close passwd file
passwd.close()
# the 3rd fd is reallocated
null = open('/dev/null')
print "NULL FD: %s" % null.fileno()
# tries to print the fileno of a closed file
try:
	print passwd.fileno()
except ValueError:
	traceback.print_exc(file=sys.stdout)
# the first fd is 3 because the 0, 1 and 2 are allocated by the stdin, stdout
# and stderr
print "Standard streams"
print "STDIN FD: %s" % sys.stdin.fileno()
print "STDOUT FD: %s" % sys.stdout.fileno()
print "STDERR FD: %s" % sys.stderr.fileno()
hosts.close()
null.close()
