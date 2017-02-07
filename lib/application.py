import os
import logging
import cherrypy
import tempfile
   
import pprint
pp = pprint.PrettyPrinter(indent=4)
   
import infrastructure.loghandlers
   
import hcconfig
import infrastructure.queuelisten
   
import interface.healthcheck
import interface.state
import interface.devices

logger = logging.getLogger('hc')
   

####################################################
# configs paths
uiIndexPath = '%s/../ui/public' % os.path.dirname(__file__)

Config = hcconfig.Config()
Listener = infrastructure.queuelisten.QueueListen()

def setupLogs(logRootDir=None):
   infrastructure.loghandlers.setupLogging(logRootDir)

def setupRoutes(disableConfigLoader=False):
   if not disableConfigLoader:
      Config.load()

   mapper = cherrypy.dispatch.RoutesDispatcher()
   
   ####################################################
   # url routes
   mapper.connect('state change node/child',
                  '/api/state/nodeid/{nodeid}/childid/{childid}',
                  controller=interface.state.StateHandler)

   mapper.connect('state change sensor',
                  '/api/state/sensor/{sensor}',
                  controller=interface.state.StateHandler)

   mapper.connect('state',
                  '/api/state',
                  controller=interface.state.StateHandler)

   mapper.connect('devices',
                  '/api/devices',
                  controller=interface.devices.DevicesHandler)

   # healthcheck route
   mapper.connect('healthcheck',
                  '/api/healthcheck',
                  controller=interface.healthcheck.HealthcheckHandler)
   
   conf = {
           '/api': {
                      'request.dispatch': mapper
                   },
           '/': {
                  'tools.staticdir.on': True,
                  'tools.staticdir.dir': uiIndexPath,
                  'tools.staticdir.index': 'index.html',
                }
          }
   return(conf)


