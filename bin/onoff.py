#!/usr/bin/python
import pprint as pp
import json
import paho.mqtt.publish as publish
import argparse


def parseArgs():
   parser = argparse.ArgumentParser(description='onoff')
   parser.add_argument('--debug', action="store_true", dest="debug")

   parser.add_argument('-n', action="store", dest="nodeid", required=True, help='The nodeid')
   parser.add_argument('-c', action="store", dest="childid", required=True, help='The childid')
   parser.add_argument('-s', action="store", dest="state", choices=['on', 'off'], required=True, help='State to set')

   args = parser.parse_args()
   return(args)


args = parseArgs()



topic = 'mygateway1-in/%s/%s/1/0/2' % (args.nodeid, args.childid)

print topic
print args.state

if args.state == 'on':
   state = 1
else:
   state = 0

r = publish.single(topic, state, hostname="localhost")

