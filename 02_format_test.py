#!/usr/bin/env python

import logging

### Ref: https://docs.python.org/3/library/logging.html#logrecord-attributes

# Interesting attributes to display...
formats= [
    'Time %(asctime)30s',
    'File %(filename)30s',
    'Func %(funcName)30s',
    'Lvl %(levelname)31s',
    'Line %(lineno)30d',
    'Mod %(module)31s',
    'Name %(name)30s',
    'Path %(pathname)30s',
    'Proc ID %(process)27d',
    'Process Name %(processName)22s',
]


DELIMIT = '\n\t'
resulting_format = 'LOG START' + DELIMIT
resulting_format += DELIMIT.join(formats)
resulting_format += '\n'
resulting_format += '  *** MESSAGE: %(message)s'

logging.basicConfig(
    level=logging.INFO,
    format=resulting_format
)

logging.info("hello world")


# $ ./02_format_test.py 
# LOG START
# 	Time        2020-03-28 19:44:26,338
# 	File              02_format_test.py
# 	Func                       <module>
# 	Lvl                            INFO
# 	Line                             33
# 	Mod                  02_format_test
# 	Name                           root
# 	Path            ./02_format_test.py
# 	Proc ID                       11827
# 	Process Name            MainProcess
#   *** MESSAGE: hello world

