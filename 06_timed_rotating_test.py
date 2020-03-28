#!/usr/bin/env python

import sys
import logging

from logging.handlers import TimedRotatingFileHandler

log = logging.getLogger('test')
log.setLevel(logging.DEBUG) # Max output


# Ref: https://docs.python.org/2/library/logging.handlers.html#timedrotatingfilehandler

# Rotates every 1 second with up to 3 backups. In practice this should have bigger when and interval values
timed_handler = TimedRotatingFileHandler('timed_rotating.log', when='S', interval=1, backupCount=3)
timed_handler.setFormatter(logging.Formatter('%(filename)s: %(message)s'))
log.addHandler(timed_handler)

# 200 bytes
log.info("1234567890123456789012") # This line is 50 bytes
log.info("1234567890123456789012") # This line is 50 bytes
log.info("1234567890123456789012") # This line is 50 bytes
log.info("1234567890123456789012") # This line is 50 bytes

# $ for x in 1 2 3 4 5; do echo "Logging, wait 2 seconds..."; ./06_timed_rotating_test.py && ls -l timed_rotating.log*; sleep 2; done
# Logging, wait 2 seconds...
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log
# Logging, wait 2 seconds...
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-50
# Logging, wait 2 seconds...
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-50
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-52
# Logging, wait 2 seconds...
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-50
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-52
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-54
# Logging, wait 2 seconds...
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-52
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-54
# -rw-r--r--  1   200 28 Mar 21:13 timed_rotating.log.2020-03-28_21-13-56
