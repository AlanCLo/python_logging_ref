#!/usr/bin/env python

import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s: %(message)s'
)
logging.info("hello world")


console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('CONSOLE HANDLER %(name)s: %(message)s'))

propagate_log = logging.getLogger('propagate_log')
propagate_log.addHandler(console_handler)
propagate_log.info('Message for propagate_log')


stand_alone_log = logging.getLogger('stand_alone_log')
stand_alone_log.propagate = False
stand_alone_log.addHandler(console_handler)
stand_alone_log.info('Message for stand_alone_log')

# $ ./03_progagate_test.py
# root: hello world
# CONSOLE HANDLER propagate_log: Message for propagate_log
# propagate_log: Message for propagate_log
# CONSOLE HANDLER stand_alone_log: Message for stand_alone_log
