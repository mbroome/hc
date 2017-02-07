import os
import urllib
import json
import logging
import cherrypy
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application

import infrastructure.requestutils

import controller.devices

logger = logging.getLogger('hc.' + __name__)

class DevicesHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      devices = controller.devices.Controller(args)

      r = devices.get(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))


