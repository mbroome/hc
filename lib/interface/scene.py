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

import controller.scene

logger = logging.getLogger('hc.' + __name__)

class SceneListHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      scene = controller.scene.Controller(args)

      r = scene.get(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))

class SceneExecHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      scene = controller.scene.Controller(args)

      r = scene.run(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))


