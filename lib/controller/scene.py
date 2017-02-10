
import logging

import base64
import time
import re

import cherrypy
import paho.mqtt.publish as publish

import application
import scenes
import infrastructure.workerpool

from infrastructure.exceptions import *

import pprint
pp = pprint.PrettyPrinter(indent=4)

logger = logging.getLogger('hc.' + __name__)

class Controller():
   def __init__(self, requestConfig={}):
      self.requestConfig = requestConfig


   ###############################################################
   def get(self, requestConfig={}):
      response = []
      for s in scenes.scenes:
         response.append({'id': s, 'description': scenes.scenes[s].description})

      return(response)

   def run(self, requestConfig={}):
      response = {}

      if scenes.scenes.has_key(requestConfig['scene']):
         response = infrastructure.workerpool.Pool.add(requestConfig, 'scene')

      return(response)


