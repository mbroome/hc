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

import controller.state

logger = logging.getLogger('hc.' + __name__)

class StateHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      state = controller.state.Controller(args)

      r = state.get(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))

   def POST(self, **args):
      state = controller.state.Controller(args)

      if args.has_key('body'):
         content = args['body']
      else:
         content = urllib.unquote_plus(cherrypy.request.body.read())
         if len(content) <= 0:
            for k in cherrypy.request.body_params:
               content = k
               break

      try:
         params = content.split('=')
         args[params[0]] = params[1]
      except:
         pass

      if args.has_key('nodeid') and args.has_key('childid'):
         device = '%s:%s' % (args['nodeid'], args['childid'])
      elif args.has_key('sensor'):
         device = args['sensor']
         parts = args['sensor'].split(':')
         args['nodeid'] = parts[0]
         args['childid'] = parts[1]

      args['device'] = device

      r = state.post(args)

      response = {'status': 'success', 'data': r, 'message': None}

      return(json.dumps(response))


