#!/usr/bin/env python3
#launchterms.py [numterms [path]]

import argparse
import os
import re
import subprocess
import sys
from tkinter import filedialog

#usage: launchterms.py [-n] [path]
#-n will just use path
#path will change path to specified instead of default

DEFAULTNUM = "3" #is a string for argument, gets converted same as
DEFAULTSIZE = "80x79"
DEFAULTLOC = "+0+0" #also accept '@' on the end to specify monitor

def parseinitialloc(s):
   pattern = r"^([+-]\d+)([+-]\d+)$"
   match = re.match(pattern, s)
   if not match:
      return 0,0
   x,y = match.groups()
   return x, y

p = argparse.ArgumentParser("launch group of xterms in specified directory")
p.add_argument("-n", "--numterms", help="number of terminals to launch", default=DEFAULTNUM)
p.add_argument("-s", "--size", help="size of terminal, CHARxROW", default=DEFAULTSIZE)
p.add_argument("-i", "--initialdir", help="initial directory for selector")
p.add_argument("-l", "--location", help="initial location of first window, default +0+0", default=DEFAULTLOC)
p.add_argument("-xrm", "--xrmstring", help="x resource string for xterms. usually 'Page:desk p_off_x p_off_y'")
p.add_argument("-r", "--resourcename", help="resource name")
p.add_argument("-d", "--startingdir", help="start terminals in this directory, don't ask")
args = p.parse_args()
if args.startingdir:
   directory = os.path.expanduser(args.startingdir)
else: 
   if args.initialdir:
      startdir = os.path.expanduser(args.initialdir)
   else:
      startdir = os.path.expanduser('~')
   directory = filedialog.askdirectory(initialdir=startdir)
try: #if dir is empty, will start in cwd
   os.chdir(directory)
except:
   print("Couldn't chdir to directory: ",directory)

#if first character of initial location is - count down else count up
if args.location[0] == '-':
    direction = -1
else:
    direction = 1

initialx, initialy = parseinitialloc(args.location)

width = int(args.size.split('x')[0])
xdist = (width * 6) + 14  #originally 494

for i in range(int(args.numterms)):
   xpos = int(initialx) + (i * direction * xdist)#6 pixels wide per character plus 14
   if xpos < 0:
      position = f"{args.size}{xpos}{initialy}"
   else:
      position = f"{args.size}{args.location[0]}{xpos}{initialy}"
   print(xpos, initialy, position)
   execargs = ['xterm', '-geometry', position]
   if args.xrmstring != None:
      execargs.append('-xrm')
      execargs.append(args.xrmstring)
   if args.resourcename != None:
      execargs.append('-name')
      execargs.append(args.resourcename)
   subprocess.Popen(execargs)
