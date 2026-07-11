#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from tkinter import filedialog

#usage: launchterms.py [-n] [path]
#-n will just use path
#path will change path to specified instead of default

DEFAULTPATH = "~/SyncDir/software"
ask = True

p = argparse.ArgumentParser("launch group of xterms in specified directory")
p.add_argument('-n', action='store_true', help="don't bring up a window to ask for pwd")
p.add_argument('-xrm', help="x resource string for xterms. usually 'Page:desk p_off_x p_off_y'")
p.add_argument('dir', nargs='?', const=None, default=DEFAULTPATH, help="xterm's pwd")
args = p.parse_args()
print(args)

directory = os.path.expanduser(args.dir)
try:
   os.chdir(directory)
except:
   print("Couldn't chdir to: ",directory)
if args.n == False:
   directory = filedialog.askdirectory()
if len(directory) > 0:
   try:
      os.chdir(directory) 
   except:
      print("Couldn't chdir to selected: ",directory)

   xcmd = ['xterm']
   if args.xrm != None:
      xcmd.extend(['-xrm', args.xrm])
   xtermargs = xcmd[:]
   xtermargs.extend(['-geometry', '80x79+0+0'])
   print(xtermargs)
   subprocess.Popen(xtermargs)
   xtermargs = xcmd[:]
   xtermargs.extend(['-geometry', '80x79+494+0'])
   subprocess.Popen(xtermargs)
   xtermargs = xcmd[:]
   xtermargs.extend(['-geometry', '80x79+988+0'])
   subprocess.Popen(xtermargs)
   xtermargs = xcmd[:]
   xtermargs.extend(['-geometry', '80x79+1482+0'])
   subprocess.Popen(xtermargs)
   xtermargs = xcmd[:]
   xtermargs.extend(['-geometry', '80x79+1976+0'])
   subprocess.Popen(xtermargs)
   xtermargs = xcmd[:]
   xtermargs.extend(['-geometry', '80x79+2470+0'])
   subprocess.Popen(xtermargs)
   xtermargs = xcmd[:]
   xtermargs.extend(['-geometry', '80x79+2964+0'])
   subprocess.Popen(xtermargs)
#   subprocess.Popen(['xterm', '-geometry', '80x79+0+0'])
#   subprocess.Popen(['xterm', '-geometry', '80x79+494+0'])
#   subprocess.Popen(['xterm', '-geometry', '80x79+988+0'])
#   subprocess.Popen(['xterm', '-geometry', '80x79+1482+0'])
#   subprocess.Popen(['xterm', '-geometry', '80x79+1976+0'])
#   subprocess.Popen(['xterm', '-geometry', '80x79+2470+0'])
#   subprocess.Popen(['xterm', '-geometry', '80x79+2964+0'])
