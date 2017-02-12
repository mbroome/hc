import os
import glob
import imp

import pprint
pp = pprint.PrettyPrinter(indent=4)

scenes = {}
libPath = os.path.realpath(os.path.dirname(__file__))

flist = glob.glob('%s/*.py' % libPath)
      
modules = {}

for file in flist:
   if not file[-11:] == '__init__.py':
      parts = file.split('/')
      name = parts[len(parts) - 1]
      name = name[:len(name) - 3]
      modules[name] = True

for module in modules:
   if modules[module]:
      f, filename, desc = imp.find_module(module, [libPath])
      scenes[module] = imp.load_module(module, f, filename, desc)


