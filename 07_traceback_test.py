#!/usr/bin/env python

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s: %(message)s'
)


log = logging.getLogger('test')

def make_error(x:int):
    try:
        result = x / 0
    except ZeroDivisionError as e:
        log.exception(e) # exception() is level ERROR

make_error(1)

# $ ./07_traceback_test.py 
# test: division by zero
# Traceback (most recent call last):
#   File "./07_traceback_test.py", line 15, in make_error
#     result = x / 0
# ZeroDivisionError: division by zero
