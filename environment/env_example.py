#!/usr/bin/env python

import os

# print $HOME environment variable
print os.getenv("HOME")
# print $MESSAGE env variable
msg = os.getenv("MESSAGE")
print msg if msg else "$ export MESSAGE=\"your message here\""
os.putenv("RET_MSG", "returning a msg")
os.system("echo $RET_MSG")
print os.environ["PATH"]
print os.environ.has_key("EDITOR")
