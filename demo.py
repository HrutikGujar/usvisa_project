from us_visa.logger import logging
from us_visa.exception import USVISAException
import sys

#logging.info("Demo file is run")
#logging.info("Another info log from demo file")


try:
    a = 5 / 0
except Exception as e:   
    raise USVISAException(e, sys)

