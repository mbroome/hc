import os
import json
import logging
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application

import controller.state

logger = logging.getLogger('hc.' + __name__)

config = {'sensor': '6:5'}

def run(args):
   state = controller.state.Controller(args)

   if args['value']:
      logger.info('trigger: %s: should disable pump while filling' % __name__) 

      r = state.post({'nodeid': 6, 'childid': 6, 'state': 0})



