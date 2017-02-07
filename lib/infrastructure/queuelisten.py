import pprint as pp
import time
import json
import paho.mqtt.client as mqtt
import logging
   
logger = logging.getLogger('hc.' + __name__)
   
import triggers

stateFile = '/home/pi/paho-mqtt/state.json'
devicesFile = '/home/pi/paho-mqtt/devices.json'
mySensorsFile = '/home/pi/paho-mqtt/mysensors-map.json'
   
   
class RecursiveDict(dict):
    """Implementation of perl's autovivification feature."""
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
   
class QueueListen():
   def __init__(self):
      self.state = RecursiveDict()
      self.devices = RecursiveDict()
      self.mySensorsMap = {}
   
      self.client = mqtt.Client()
      self.client.on_connect = self.on_connect
      self.client.on_message = self.on_message

      self.load()

   def triggerLookup(self, sensor):
      for t in triggers.triggers:
         if triggers.triggers[t].config['sensor'] == sensor:
            logger.info('found a matching trigger: %s' % sensor)
            triggers.triggers[t].run(self.state[sensor])

   def parse(self, topic, v):
      #print topic
      p = topic.split('/')
      try:
         value = float(v)
      except:
         value = v
   
      tmap =  self.mySensorsMap['n2s']['mysensor_internal']
      k = '%s:%s' % (p[1], p[2])
      msgType = self.mySensorsMap['n2s']['mysensor_command'][p[3]]
   
      #logger.info('%s => %s => %s' % (msgType, topic, v))
   
      try:
         if msgType == 'C_PRESENTATION':
            if p[2] != '255':
               self.devices['sensors'][k]['nodeid'] = p[1]
               self.devices['sensors'][k]['childid'] = p[2]
               self.devices['sensors'][k]['name'] = value
               self.devices['sensors'][k]['type'] = p[5]
               self.devices['sensors'][k]['time'] = time.time()
         elif msgType == 'C_INTERNAL':
            self.devices['nodes'][p[1]][tmap[p[5]]] = value
            self.devices['nodes'][p[1]]['time'] = time.time()
         elif msgType == 'C_SET':
            self.state[k]['id'] = k
            self.state[k]['nodeid'] = p[1]
            self.state[k]['childid'] = p[2]
            self.state[k]['time'] = time.time()
            try:
               if self.state[k]['value'] != value:
                  self.state[k]['change'] = True
               else:
                  self.state[k]['change'] = False
            except Exception, e:
               logger.exception(e)
               self.state[k]['change'] = False

            self.state[k]['value'] = value

            if self.state[k]['change']:
               self.triggerLookup(k)

      except Exception, e:
         logger.exception(e)
   
   # The callback for when the client receives a CONNACK response from the server.
   def on_connect(self, client, userdata, flags, rc):
      #print("Connected with result code "+str(rc))
   
      # Subscribing in on_connect() means that if we lose the connection and
      # reconnect then subscriptions will be renewed.
      #client.subscribe("$SYS/#")
      client.subscribe("mygateway1-out/#")
   
   # The callback for when a PUBLISH message is received from the server.
   def on_message(self, client, userdata, msg):
      #print(msg.topic+" "+str(msg.payload))
      #pp.pprint(msg)
   
      #logger.info('topic: %s payload: %s' % (msg.topic, msg.payload))
      self.parse(msg.topic, msg.payload)
      self.save()

   
   def save(self):
      #logger.info('saving queue data')
      try:
         fd = open(stateFile, 'w')
         fd.write(json.dumps(self.state))
         fd.close()
      except:
         pass
   
      try:
         fd = open(devicesFile, 'w')
         fd.write(json.dumps(self.devices))
         fd.close()
      except:
         pass
   
   
      #print "\n"
      #pp.pprint(devices)
   
      #print "\n\n"
   
   def load(self):
      content = open(mySensorsFile, 'r').read()
      self.mySensorsMap = json.loads(content)
   
      try:
         content = open(stateFile, 'r').read()
         self.state = json.loads(content)
      except:
         pass
      try:
         content = open(devicesFile, 'r').read()
         self.devices = json.loads(content)
      except:
         pass
   
   def listen(self):
      #pp.pprint(triggers.triggers)

      self.client.connect("localhost", 1883, 60)
   
      self.client.loop_start()


