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

   logger.info('scene: %s: water change on zone 1: %s' % (__name__, json.dumps(args)))


