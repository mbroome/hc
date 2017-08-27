import os
import json
import logging
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application

import controller.state

logger = logging.getLogger('hc.' + __name__)

description = "All zones water change"

def run(args):
   state = controller.state.Controller(args)

   logger.info('Scene ON: %s: %s' % (__name__, description))
   r = state.post({'nodeid': 6, 'childid': 5, 'state': 1})
   time.sleep(5)

   # zone 2
   logger.info('Scene: %s: zone 2' % __name__)
   r = state.post({'nodeid': 6, 'childid': 2, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 6, 'childid': 2, 'state': 0})

   time.sleep(30)

   # zone 3
   logger.info('Scene: %s: zone 3' % __name__)
   r = state.post({'nodeid': 6, 'childid': 3, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 6, 'childid': 3, 'state': 0})

   time.sleep(30)

   # zone 4
   logger.info('Scene: %s: zone 4' % __name__)
   r = state.post({'nodeid': 8, 'childid': 0, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 8, 'childid': 0, 'state': 0})

   time.sleep(30)

   # zone 5
   logger.info('Scene: %s: zone 5' % __name__)
   r = state.post({'nodeid': 8, 'childid': 1, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 8, 'childid': 1, 'state': 0})

   time.sleep(30)

   # zone 6
   logger.info('Scene: %s: zone 6' % __name__)
   r = state.post({'nodeid': 6, 'childid': 4, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 6, 'childid': 4, 'state': 0})

   logger.info('Scene OFF: %s: %s' % (__name__, description))
   r = state.post({'nodeid': 6, 'childid': 5, 'state': 0})

