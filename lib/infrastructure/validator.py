import logging

import pprint
pp = pprint.PrettyPrinter(indent=4)

from infrastructure.loghandlers import audit

logger = logging.getLogger('buildmanager.' + __name__)

def validate(data, key):
   response = True

   if type(key) is str:
      try:
         if not data.has_key(key):
            logger.info('validation failed: key: %s => data: %s' % (key, data))
            return((False, key))
      except:
         pass
   elif type(key) is list:
      for k in key:
         try:
            if not data.has_key(k):
               logger.info('validation failed: key: %s => data: %s' % (k, data))
               return((False, k))
         except:
            pass

   return((True, None))

def oneof(data, keylist):
   for k in keylist:
      try:
         if data.has_key(k):
            return((True, None))
      except:
         pass

   logger.info('validation failed: key: %s => data: %s' % (keylist, data))
   return((False, keylist))

