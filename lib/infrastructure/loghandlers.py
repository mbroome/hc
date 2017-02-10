import os
import logging
import json
import inspect

import cherrypy

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application

def setupLogging(logRootDir):
   logger = logging.getLogger('hc')

   if not logRootDir:
      logRootDir = '/var/log'

   try:
      os.makedirs(logRootDir + '/hc')
   except:
      pass

   application.Config.logRootDir = logRootDir

   # setup the standard logger
   hdlr = logging.FileHandler('%s/hc.log' % logRootDir)
   formatter = logging.Formatter('%(asctime)s: %(message)s', datefmt='%s')
   hdlr.setFormatter(formatter)
   logger.addHandler(hdlr)
   logger.setLevel(logging.INFO)


