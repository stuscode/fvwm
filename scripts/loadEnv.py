#!/usr/bin/env python3

import os
import sys

#with open('/home/stew/fvwmdebug','w') as d:
#   print("here",file=d)
#   print(sys.argv[0],file=d)
#   print("here",file=d)
#   print(sys.argv[1],file=d)
#   print("here",file=d)
with open(sys.argv[1], 'r') as f:
   for l in f:
      e,v = l.rstrip().split('=')
      print('setEnv', e, v)
#      print('InfoStoreAdd', e, v)
