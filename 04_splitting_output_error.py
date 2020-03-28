#!/usr/bin/env python

import sys
import logging

log = logging.getLogger('test')
log.setLevel(logging.DEBUG) # Max output


stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(logging.Formatter('STDOUT %(name)s: %(message)s'))
stdout_handler.setLevel(logging.INFO)
# setLevel(logging.INFO) is effectively record.levelno >= logging.INFO
stdout_handler.addFilter(lambda record: record.levelno <= logging.INFO)
log.addHandler(stdout_handler)

stderr_handler = logging.StreamHandler() # Default is stderr
stderr_handler.setFormatter(logging.Formatter('STDERR %(name)s: %(message)s'))
stderr_handler.setLevel(logging.ERROR)
log.addHandler(stderr_handler)


log.debug("debug")        # Ignored by both because of level >=INFO and >=ERROR
log.info("info")          # Only in stdout because stderr is level >=ERROR
log.warning("warning")    # Ignored by both. stdout filter <= INFO. stderr level >=ERROR
log.error("error")        # Only in stderr because of level >=ERROR
log.critical("critical")  # Only in stderr because of level >=ERROR


# $ ./04_splitting_output_error.py 
# STDOUT test: info
# STDERR test: error
# STDERR test: critical
#
# $ ./04_splitting_output_error.py 2> /dev/null
# STDOUT test: info
# 
# $ ./04_splitting_output_error.py > /dev/null
# STDERR test: error
# STDERR test: critical


