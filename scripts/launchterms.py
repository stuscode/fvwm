#!/usr/bin/env python3

import os
import subprocess
import sys
from tkinter import *
from tkinter import filedialog

DEFAULTPATH = "~/SyncDir/software"

window = Tk()
if len(sys.argv) > 1:
   path = sys.argv[1]
else:
   path = DEFAULTPATH
startpath = os.path.expanduser(path)
os.chdir(startpath)
directory = filedialog.askdirectory()
if len(directory) > 0:
   os.chdir(directory) 
   subprocess.Popen(['xterm', '-geometry', '80x79+0+0'])
   subprocess.Popen(['xterm', '-geometry', '80x79+494+0'])
   subprocess.Popen(['xterm', '-geometry', '80x79+988+0'])
   subprocess.Popen(['xterm', '-geometry', '80x79+1482+0'])
   subprocess.Popen(['xterm', '-geometry', '80x79+1976+0'])
   subprocess.Popen(['xterm', '-geometry', '80x79+2470+0'])
   subprocess.Popen(['xterm', '-geometry', '80x79+2964+0'])
