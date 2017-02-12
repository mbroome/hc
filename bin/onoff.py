#!/usr/bin/env python
import os
import sys
import pprint as pp
import json
import argparse

# account for where we live including the lib path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
sys.path.append(scriptPath + '/../lib/')


import controller.state

def parseArgs():
   parser = argparse.ArgumentParser(description='onoff')
   parser.add_argument('--debug', action="store_true", dest="debug")

   parser.add_argument('--sensor', action="store", dest="sensor", required=True, help='The sensorid')
   parser.add_argument('--state', action="store", dest="state", choices=['on', 'off'], required=True, help='State to set')

   args = parser.parse_args()
   return(args)


args = parseArgs()


state = controller.state.Controller(args)

# build up a request to look like a normal post
request = {}
device = args.sensor
parts = args.sensor.split(':')
request['nodeid'] = parts[0]
request['childid'] = parts[1]

request['device'] = device

if args.state == 'on':
   request['state'] = 1
else:
   request['state'] = 0

# make the request
r = state.post(request)



