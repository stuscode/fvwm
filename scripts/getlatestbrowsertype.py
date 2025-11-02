#!/usr/bin/python3

import subprocess
import sys

BrowserVar = "InfoStoreAdd WHICHBROWSER "
configdirs = { "brave": ".config/BraveSoftware",
               "chrome"  : ".config/google-chrome",
               "chromium": ".config/Chromium",
               "firefox" : ".mozilla" 
             }

def usage():
   print("usage: getlatestbrowsertype.py browser")
   exit(1)

#Argument is the type of browser (firefox, brave, etc)  Something that 
#string matches a process name.
#Find the newest process that matches, then look for the loopback
#mount of the browser config directory in /proc/pid/mountinfo
#finally find the name of the instance as the directory name where 
#the profile is stored

#if len(sys.argv) != 2:
#   usage()

try:
   destdir = configdirs[sys.argv[1]]
except KeyError:
   print(BrowserVar, "unknown1")
   exit(0)
#   print("browser type not found.  Edit this executable and add map to configdirs")
#   usage()

psout = subprocess.Popen(["ps","-eo","command,pid","--sort=etime"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
for line in psout.stdout:
   if  sys.argv[1] in line:
      cmd,pid = line.split()
      mfile = "/proc/" + pid + "/mountinfo"
      with open(mfile, 'r') as f:
         for l in f:
            if destdir in l:
               p = l.split()
               for c in p:
                  if c[0] =='/':
                     d = c.split('/')
                     print(BrowserVar, d[-1])
                     exit(0)
#not found
print(BrowserVar, "unknown2")
