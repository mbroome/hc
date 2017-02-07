stateMap = {
   'active': 'ACTIVE',
   'shutoff': 'SHUTOFF',
   'running': 'ACTIVE',
   'stopped': 'SHUTOFF',
   'deleted': 'DELETED',
   'terminating': 'TERMINATING',
}

def state(s):
   s = s.lower()
   if stateMap.has_key(s):
      return(stateMap[s].upper())
   else:
      return(s.upper())

