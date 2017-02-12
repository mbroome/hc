
import logging

import base64
import time
import re

import cherrypy

import application
import infrastructure.workerpool

import pprint
pp = pprint.PrettyPrinter(indent=4)

logger = logging.getLogger('hc.' + __name__)

class Controller():
   def __init__(self, requestConfig={}):
      self.requestConfig = requestConfig


   ###############################################################
   def get(self, requestConfig={}):
      response = infrastructure.workerpool.Pool.status()

      return(response)


