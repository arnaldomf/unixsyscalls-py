#!/usr/bin/env python

import sys


print sys.argv
print '--help' in sys.argv
print True if '-c' in sys.argv and sys.argv[sys.argv.index('-c') + 1] else False