import os
import sys
import logging

import base64
import time
import re

import cherrypy

import application

from infrastructure.exceptions import *

import pprint
pp = pprint.PrettyPrinter(indent=4)

logger = logging.getLogger('hc.' + __name__)

class Controller():
   def __init__(self, requestConfig={}):
      self.requestConfig = requestConfig


   ###############################################################
   def get(self, requestConfig={}):
      filename = application.Config.logRootDir + '/hc.log'
      response = {}

      lines = 20
      if requestConfig.has_key('lines'):
         lines = int(requestConfig['lines'])

      try:
         fd = open(filename, 'r')


         file_size = fd.tell()
         fd.seek(max(file_size - 10*1024, 0))

         # this will get rid of trailing newlines, unlike readlines()
         buffer = fd.read().splitlines()[-lines:]

         fd.close()

         response = buffer

      except Exception, e:
         pp.pprint(e)

      return(response)



