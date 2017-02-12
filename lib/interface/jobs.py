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

import controller.jobs

logger = logging.getLogger('hc.' + __name__)

class JobsHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      jobs = controller.jobs.Controller(args)

      r = jobs.get(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))

