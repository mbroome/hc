import logging
import cherrypy
from optparse import OptionParser


logger = logging.getLogger('hc.' + __name__)


class DefaultHandler:
   # CORS kind of sucks...
   def OPTIONS(self, **args):
      cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
      cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
      cherrypy.response.headers["Access-Control-Allow-Headers"] = cherrypy.request.headers.get('Access-Control-Request-Headers')

   def __call__(self, **args):
      cherrypy.response.headers["Content-Type"] = "application/json"
      cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
      cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
      cherrypy.response.headers["Access-Control-Allow-Headers"] = cherrypy.request.headers.get('Access-Control-Request-Headers')
      return getattr(self, cherrypy.request.method.upper())(**args)

