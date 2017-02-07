import logging
import cherrypy

import infrastructure.requestutils

logger = logging.getLogger('hc.' + __name__)

class HealthcheckHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      return('OK')

