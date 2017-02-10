import logging
import time

logger = logging.getLogger('hc.' + __name__)

import pprint
pp = pprint.PrettyPrinter(indent=4)

# the base class all exceptions derive from
class BaseException(Exception):
   def __init__(self, message):
      super(BaseException, self).__init__(message)

   def to_json(self):
      return(self.message)

# lockerbox exceptions
class BucketAccessException(BaseException):
   def __init__(self, message):
      super(BucketAccessException, self).__init__(message)
      self.statuscode = 403

