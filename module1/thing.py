#!/usr/bin/env python

import logging

class Thing:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def do(self):
        self.log.debug('debug')
        self.log.info('info')
        self.log.warning('warning')
        self.log.error('error')
        self.log.critical('critical')
