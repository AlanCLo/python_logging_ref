#!/usr/bin/env python

### Levels

import logging



### Most info

#logging.basicConfig(level=logging.NOTSET)
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.WARNING)
#logging.basicConfig(level=logging.ERROR)
#logging.basicConfig(level=logging.CRITICAL)

### Least info


logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

# $ ./01_basic_test.py 
# INFO:root:info
# WARNING:root:warning
# ERROR:root:error
# CRITICAL:root:critical


