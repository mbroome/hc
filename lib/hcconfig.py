import os
import sys
import json
import base64
import threading
import logging

import cherrypy

import pprint
pp = pprint.PrettyPrinter(indent=4)

# account for where we live including the lib path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
sys.path.append(scriptPath + '/../lib/')

from infrastructure.exceptions import *

logger = logging.getLogger('hc.' + __name__)

class Config():
   def __init__(self):
      self.installDir = os.path.dirname(__file__) + '/../'
      self.configDir = '/etc/config/hc/'
      self.logRootDir = ''

   def load(self):
      self.State()
      self.Devices()

   # load up some configs
   def State(self):
      self.s = self.loadJSON('/home/pi/paho-mqtt/state.json')
      return(self.s)

   def Devices(self):
      self.d = self.loadJSON('/home/pi/paho-mqtt/devices.json')
      return(self.d)


   def loadJSON(self, configFile):
      data = {}
      try:
         contents = open(configFile, 'r').read()
         data = json.loads(contents)
      except:
         pass
      return(data)

