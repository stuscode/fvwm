#!/usr/bin/env python3

import os
import sys

with open(sys.argv[1], 'r') as f:
   for l in f:
      e,v = l.rstrip().split('=')
      print('setEnv', e, v)
      key,winid = e.split('-')
      print('Echo exec BrowserUseName', winid)
      print('Function BrowserUseName', winid)
#      print('InfoStoreAdd', e, v)
