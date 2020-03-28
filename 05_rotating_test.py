#!/usr/bin/env python

import sys
import logging

from logging.handlers import RotatingFileHandler

log = logging.getLogger('test')
log.setLevel(logging.DEBUG) # Max output


rotating_handler = RotatingFileHandler('rotating.log', maxBytes=300, backupCount=3)
rotating_handler.setFormatter(logging.Formatter('%(filename)s: %(message)s'))
log.addHandler(rotating_handler)

# Output 200 bytes
log.info("1234567890123456789012345678") # This line is 50 bytes
log.info("1234567890123456789012345678") # This line is 50 bytes
log.info("1234567890123456789012345678") # This line is 50 bytes
log.info("1234567890123456789012345678") # This line is 50 bytes


# $ ./05_rotating_test.py && ls -lh rotating.log*
# -rw-r--r--  1    200B 28 Mar 20:59 rotating.log
# $ ./05_rotating_test.py && ls -lh rotating.log*
# -rw-r--r--  1    150B 28 Mar 20:59 rotating.log
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.1
# $ ./05_rotating_test.py && ls -lh rotating.log*
# -rw-r--r--  1    100B 28 Mar 20:59 rotating.log
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.1
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.2
# $ ./05_rotating_test.py && ls -lh rotating.log*
# -rw-r--r--  1     50B 28 Mar 20:59 rotating.log
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.1
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.2
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.3
# $ ./05_rotating_test.py && ls -lh rotating.log*
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.1
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.2
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.3
# $ ./05_rotating_test.py && ls -lh rotating.log*
# -rw-r--r--  1    200B 28 Mar 20:59 rotating.log
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.1
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.2
# -rw-r--r--  1    250B 28 Mar 20:59 rotating.log.3
# 

