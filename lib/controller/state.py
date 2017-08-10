
import logging

import base64
import time
import re

import paho.mqtt.publish as publish

import application

from infrastructure.exceptions import *

import pprint
pp = pprint.PrettyPrinter(indent=4)

logger = logging.getLogger('hc.' + __name__)

stateMap = {'0': 'off',
            '1': 'on',
             0: 'off',
             1: 'on'}

class Controller():
   def __init__(self, requestConfig={}):
      self.requestConfig = requestConfig


   ###############################################################
   def get(self, requestConfig={}):
      response = application.Listener.state.copy()

      return(response)

   def post(self, requestConfig={}):
      response = {'type': 'post'}

      topic = 'mygateway1-in/%s/%s/1/0/2' % (requestConfig['nodeid'], requestConfig['childid'])

      sensor = '%s:%s' % (requestConfig['nodeid'], requestConfig['childid'])
      devices = application.Config.Devices()
      name = devices['sensors'][sensor]['name']

      logger.info('State change (controller): name: %s => sensor: %s state: %s' % (name, sensor, stateMap[requestConfig['state']]))
      r = publish.single(topic, requestConfig['state'], hostname="localhost")


      return(response)


