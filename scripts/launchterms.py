#!/usr/bin/env python3
#launchterms.py [numterms [path]]

import os
import subprocess
import sys
from tkinter import filedialog

PATH = "~/SyncDir/software"
NUMTERMS = 3

if len(sys.argv) > 1:
   NUMTERMS = int(sys.argv[1])
if len(sys.argv) > 2:
   PATH = sys.argv[2]

if len(sys.argv) < 3:
   PATH = filedialog.askdirectory()
directory = os.path.expanduser(PATH)
try:
   os.chdir(directory)
except:
   print("Couldn't chdir to: ",directory)
if len(directory) > 0:
   try:
      os.chdir(directory) 
   except:
      print("Couldn't chdir to selected: ",directory)
   for i in range(NUMTERMS):
      xpos = i * 494
      position = f"80x79+{xpos}+0"
      subprocess.Popen(['xterm', '-geometry', position])
#   subprocess.Popen(['xterm', '-geometry', '80x79+0+0'])
#   subprocess.Popen(['xterm', '-geometry', '80x79+494+0'])
#   subprocess.Popen(['xterm', '-geometry', '80x79+988+0'])
