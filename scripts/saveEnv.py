#!/usr/bin/env python3

import os
import sys

parent = str(os.getppid())
with open(sys.argv[1], 'w') as o:
   with open('/proc/'+parent+'/environ', 'r') as f:
      envs = f.read()
      s = envs.split('\x00')
      for e in s:
         if 'browsername' in e:
            print(e, file=o)
