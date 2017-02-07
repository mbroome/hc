import os
import json
import logging
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application

import controller.state

logger = logging.getLogger('hc.' + __name__)

config = {'sensor': '8:0'}

def run(args):
   state = controller.state.Controller(args)

   logger.info('trigger data in relay1off: %s' % json.dumps(args))
   if args['value']:
      logger.info('trigger should disable relay') 

   r = state.post({'nodeid': args['nodeid'], 'childid': args['childid'], 'state': 0})

   pp.pprint(r)


