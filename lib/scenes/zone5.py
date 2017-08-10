import os
import json
import logging
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application

import controller.state

logger = logging.getLogger('hc.' + __name__)

description = "Zone 5 water change"

def run(args):
   state = controller.state.Controller(args)

   logger.info('Scene: %s: %s' % (__name__, description))

   # turn the pump on
   #r = state.post({'nodeid': 6, 'childid': 6, 'state': 1})
   #time.sleep(30)

   # turn on zone 5
   r = state.post({'nodeid': 8, 'childid': 1, 'state': 1})

   # wait a hour
   time.sleep(60*10)

   # turn off zone 5
   r = state.post({'nodeid': 8, 'childid': 1, 'state': 0})
   # and turn off the pump
   #r = state.post({'nodeid': 6, 'childid': 6, 'state': 0})

