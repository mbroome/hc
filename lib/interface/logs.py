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

import controller.logs

logger = logging.getLogger('hc.' + __name__)

class LogsHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      logs = controller.logs.Controller(args)

      r = logs.get(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))


