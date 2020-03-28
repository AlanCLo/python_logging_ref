#!/usr/bin/env python

# Ref: https://simpletutorials.com/c/1457/Python+3+Logging+using+DictConfig

import logging
import logging.config

from module1.thing import Thing

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'},
        'errors': {'format': 'ERROR: %(asctime)s - %(name)s - %(message)s'}
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'dict_file.log',
            'maxBytes': 500,
            'backupCount': 1
        },
        'errors_only': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'errors',
            'filename': 'dict_errors_only.log',
            'maxBytes': 500,
            'backupCount': 1
        },
    },
    'loggers': {
        # The root logger that all other loggers inherit from
        '': {
            'level': 'INFO',
            'handlers': ['console']
        },
        'default': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'errors_only'],
            'propagate': False  
        },
        'module1': {
            'level': 'WARNING',
            ### module1 will inherit from '' and get console handler by default
            ### If you want to set handler with 'console', then you need to
            ### set 'propagate': False so that we don't see it twice
            #'handlers': ['console'], 'propagate': False  
        },
    },
    'disable_existing_loggers': False
})

# default is on debug (max) and has all handlers
log = logging.getLogger('default')
log.debug('debug')
log.info('info')
log.warning('warning')
log.error('error')
log.critical('critical')

# another_logger will inherit from ''
# It only has console handler and INFO level
another_log = logging.getLogger('another_logger')
another_log.debug('debug')
another_log.info('info')
another_log.warning('warning')
another_log.error('error')
another_log.critical('critical')

# module1 inherits from '' to get console handler
# But it also is set to WARNING level in the dictConfig
t = Thing()
t.do()


# $ ./08_dictConfig_test.py 
# 2020-03-28 22:14:58 - default - DEBUG - debug
# 2020-03-28 22:14:58 - default - INFO - info
# 2020-03-28 22:14:58 - default - WARNING - warning
# 2020-03-28 22:14:58 - default - ERROR - error
# 2020-03-28 22:14:58 - default - CRITICAL - critical
# 2020-03-28 22:14:58 - another_logger - INFO - info
# 2020-03-28 22:14:58 - another_logger - WARNING - warning
# 2020-03-28 22:14:58 - another_logger - ERROR - error
# 2020-03-28 22:14:58 - another_logger - CRITICAL - critical
# 2020-03-28 22:14:58 - module1.thing - WARNING - warning
# 2020-03-28 22:14:58 - module1.thing - ERROR - error
# 2020-03-28 22:14:58 - module1.thing - CRITICAL - critical
 
# $ cat dict_file.log 
# 2020-03-28 22:14:58 - default - DEBUG - debug
# 2020-03-28 22:14:58 - default - INFO - info
# 2020-03-28 22:14:58 - default - WARNING - warning
# 2020-03-28 22:14:58 - default - ERROR - error
# 2020-03-28 22:14:58 - default - CRITICAL - critical
 
# $ cat dict_errors_only.log 
# ERROR: 2020-03-28 22:14:58,682 - default - error
# ERROR: 2020-03-28 22:14:58,682 - default - critical
