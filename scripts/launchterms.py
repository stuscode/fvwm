#!/usr/bin/env python3
#launchterms.py [numterms [path]]

import argparse
import os
import subprocess
import sys
from tkinter import filedialog

#usage: launchterms.py [-n] [path]
#-n will just use path
#path will change path to specified instead of default

DEFAULTNUM = "3" #is a string for argument, gets converted same as

p = argparse.ArgumentParser("launch group of xterms in specified directory")
p.add_argument("-n", "--numterms", help="number of terminals to launch", default=DEFAULTNUM)
p.add_argument("-i", "--initialdir", help="initial directory for selector")
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
for i in range(int(args.numterms)):
   xpos = i * 494
   position = f"80x79+{xpos}+0"
   execargs = ['xterm', '-geometry', position]
   if args.xrmstring != None:
      execargs.append('-xrm')
      execargs.append(args.xrmstring)
   if args.resourcename != None:
      execargs.append('-name')
      execargs.append(args.resourcename)
   subprocess.Popen(execargs)
