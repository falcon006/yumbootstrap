#!/usr/bin/python3

import logging
from datetime import datetime
#-----------------------------------------------------------------------------

class ProgressHandler(logging.Handler):
  def emit(self, record):
    now = datetime.now()
    print ( now.strftime("[%T] ") ,  record.getMessage())

#-----------------------------------------------------------------------------
# vim:ft=python
