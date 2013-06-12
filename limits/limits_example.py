#!/usr/bin/env python

import resource
import traceback
import sys


def print_limits(resource, *limits):
	print "%s soft limit = %s" % (resource,limits[0])
	print "%s hard limit = %s" % (resource,limits[1])


# Processes have resource limits
soft,hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print_limits("Open Files", soft,hard)
print "Infinity: %s" % resource.RLIM_INFINITY
# Set soft limit of nofile
resource.setrlimit(resource.RLIMIT_NOFILE, (512, resource.RLIM_INFINITY))
soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print_limits("Open Files", soft,hard)
# Bumping soft limit of nofile
resource.setrlimit(resource.RLIMIT_NOFILE, (8192, resource.RLIM_INFINITY))
soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print_limits("Open Files", soft,hard)
# downsize hard limit
resource.setrlimit(resource.RLIMIT_NOFILE, (8192, 9216))
soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print_limits("Open Files", soft,hard)
# impossible to bump hard limit
try:
	resource.setrlimit(resource.RLIMIT_NOFILE, (8192, resource.RLIM_INFINITY))
except ValueError:
	traceback.print_exc(file=sys.stdout)
soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print_limits("Open Files", soft,hard)
# exceeding the limit
resource.setrlimit(resource.RLIMIT_NOFILE, (3, 9216))
try:
	open('/dev/null')
except IOError:
	traceback.print_exc(file=sys.stdout)
# Other limits
soft, hard = resource.getrlimit(resource.RLIMIT_NPROC)
print_limits("Processes", soft,hard)
soft, hard = resource.getrlimit(resource.RLIMIT_FSIZE)
print_limits("File Size", soft,hard)
soft, hard = resource.getrlimit(resource.RLIMIT_STACK)
print_limits("Stack Size", soft,hard)