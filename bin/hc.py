#!/usr/bin/python
import os
import sys
import argparse
import logging
import time

import cherrypy
from cherrypy.process.plugins import Monitor


import pprint
pp = pprint.PrettyPrinter(indent=4)

# account for where we live including the lib path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
sys.path.append(scriptPath + '/../lib/')

import application
import infrastructure.workerpool

logger = logging.getLogger('hc')

def parseArgs():
   parser = argparse.ArgumentParser(description='hc')
   parser.add_argument('--debug', action="store_true", dest="debug")

   parser.add_argument('-p', action="store", dest="port", default=8041, help='Port to listen on')

   args = parser.parse_args()
   return(args)

if __name__ == '__main__':
   args = parseArgs()

   # define a basic server config to use if not running in debug mode
   serverConfig={
      'engine.autoreload.on': False,
      #'engine.SIGHUP': None,
      #'engine.SIGTERM': None,
      'server.max_request_body_size' : 0,

      'server.socket_host': '0.0.0.0',
      'server.thread_pool': 10,

      'log.screen' : False,
      'log.access_file': '/var/log/hc/access.log', # disable access logging
      'log.error_file': '/var/log/hc/error.log',
      'tools.log_tracebacks.on': True
   }

   # set the port based on args
   serverConfig['server.socket_port'] = int(args.port)

   # if we are running in debug mode, do a simple start
   if args.debug:
      application.setupLogs('/tmp')
      logger.info('Started')

      application.Listener.listen()
      infrastructure.workerpool.Pool.start()

      try:
         routeConfig = application.setupRoutes()

         cfg = serverConfig.copy()
         del(cfg['log.screen'])
         del(cfg['log.access_file'])
         del(cfg['log.error_file'])
         del(cfg['server.socket_port'])
         cherrypy.config.update(cfg)
         cherrypy.quickstart(None, '/', config=routeConfig)
      except Exception, e:
         pp.pprint(e)
         #application.Config.stop()
   else:
      application.setupLogs()
      logger.info('Started')

      # run a real config
      routeConfig = application.setupRoutes()

      # if we are not disabling ssl, set it up
      serverConfig['server.socket_port'] = 8041

      cherrypy.tree.mount(None, '/', config=routeConfig)
      cherrypy.config.update(serverConfig)
      cherrypy.engine.start()
      cherrypy.engine.block()


