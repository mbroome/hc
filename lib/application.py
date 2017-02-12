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
import interface.scene
import interface.logs
import interface.jobs

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

   mapper.connect('scene run',
                  '/api/scene/run/{scene}',
                  controller=interface.scene.SceneExecHandler)

   mapper.connect('scene list',
                  '/api/scene',
                  controller=interface.scene.SceneListHandler)

   mapper.connect('jobs status',
                  '/api/jobs/status',
                  controller=interface.jobs.JobsHandler)

   mapper.connect('logs x lines',
                  '/api/logs/lines/{lines}',
                  controller=interface.logs.LogsHandler)

   mapper.connect('logs',
                  '/api/logs',
                  controller=interface.logs.LogsHandler)

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


