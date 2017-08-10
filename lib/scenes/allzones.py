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

   logger.info('Scene: %s: %s' % (__name__, description))

   # zone 2
   r = state.post({'nodeid': 6, 'childid': 2, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 6, 'childid': 2, 'state': 0})

   time.sleep(30)

   # zone 3
   r = state.post({'nodeid': 6, 'childid': 3, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 6, 'childid': 3, 'state': 0})

   time.sleep(30)

   # zone 4
   r = state.post({'nodeid': 8, 'childid': 0, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 8, 'childid': 0, 'state': 0})

   time.sleep(30)

   # zone 5
   r = state.post({'nodeid': 8, 'childid': 1, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 8, 'childid': 1, 'state': 0})

   time.sleep(30)

   # zone 6
   r = state.post({'nodeid': 6, 'childid': 4, 'state': 1})
   time.sleep(60*10)
   r = state.post({'nodeid': 6, 'childid': 4, 'state': 0})

