import os
import json
import logging
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application

import controller.state

logger = logging.getLogger('hc.' + __name__)

description = "Zone 1 water change"

def run(args):
   state = controller.state.Controller(args)

   logger.info('Scene: %s: %s' % (__name__, description))

   r = state.post({'nodeid': 8, 'childid': 0, 'state': 1})

   time.sleep(60*2)

   r = state.post({'nodeid': 8, 'childid': 0, 'state': 0})

