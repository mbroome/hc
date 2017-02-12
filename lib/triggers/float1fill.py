import os
import json
import logging
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application

import controller.state

logger = logging.getLogger('hc.' + __name__)

config = {'sensor': '6:30'}

def run(args):
   state = controller.state.Controller(args)

   if args['value']:
      logger.info('trigger: %s: should disable water fill' % __name__) 

      r = state.post({'nodeid': 6, 'childid': 5, 'state': 0})



