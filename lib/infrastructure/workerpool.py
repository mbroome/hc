import sys
import threading
import Queue
import time
import json
import logging

import pprint
pp = pprint.PrettyPrinter(indent=4)

import application
import triggers
import scenes

jobQueue = Queue.Queue()

logger = logging.getLogger('hc.' + __name__)

class PoolWorker(threading.Thread):
   def __init__(self, workerID):
      self.threadName = 'PoolWorker-' + str(workerID)
      self.status = 'idle'
      self.job = {}
      threading.Thread.__init__(self, name=self.threadName)

   def run(self):
      # watch the queue forever
      while True:
         self.status = 'waiting'
         item = jobQueue.get()
         if item == None:
            jobQueue.put(item)
            break
         message, handler = item

         try:
            if handler == 'trigger':
               self.status = 'running'
               self.job = {'type': 'trigger', 'id': message['trigger'], 'time': time.time()}

               r = triggers.triggers[message['trigger']].run(message)
            elif handler == 'scene':
               self.status = 'running'
               self.job = {'type':'scene', 'id': message['scene'], 'time': time.time()}

               r = scenes.scenes[message['scene']].run(message)
         except Exception, e:
            logger.exception('Error in message handler: %s' % e)

         self.status = 'idle'
         self.job = {}

class PoolManager():
   def __init__(self, poolSize=20):
      self.poolSize = poolSize
      self.workerList = {}

   def start(self):
      logger.info('#### Workerpool started')
      for i in range(self.poolSize):
         t = PoolWorker(i)
         t.daemon = True
         t.start()
         self.workerList[i] = t

   def add(self, message, handler):
      jobQueue.put((message, handler))

   def exit(self):
      jobQueue.put(None)

   def status(self):
      response = {'threads': {}, 'jobs': {}}
      for i in self.workerList:
         response['threads'][i] = self.workerList[i].status
         if self.workerList[i].job.has_key('id'):
            response['jobs'][self.workerList[i].job['id']] = self.workerList[i].job
      return(response)

Pool = PoolManager()

