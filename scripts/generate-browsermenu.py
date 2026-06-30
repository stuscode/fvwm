#!/usr/bin/env python3

import argparse
import os
import signal
import subprocess
import sys
import time
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
from tkinter import simpledialog

DEFAULTPATH="~/browserdirs"

def new_browser(root, basedir, browser):
   profile = simpledialog.askstring("Input", "New Profile Name:")
   launch(root, basedir, browser, profile, "keep")

def handle_ctrl_c(event):
   sys.exit(0)     # Exit the Python process`

def check_for_int(root):
   root.after(100, lambda: check_for_int(root))

class browserlist:
   def __init__(self):
      self.name = ""
      self.list = []

def launch(root, basedir, browser, profile, disp):
   command = "start_browser"
   clist = [command]
   if disp == "erase":
      clist.append("-r")
   clist.append(browser)
   clist.append(os.path.join(basedir, browser))
   clist.append(profile)
   root.withdraw()
   #root.update, root.deiconify to redisplay
   p = subprocess.Popen(clist, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   for t in range(20):
      time.sleep(1)
      status = p.poll()
      if status != None:
         out,err = p.communicate()
         commandline = " ".join(clist)
         tk.messagebox.showerror("Browser launch", f"command: {commandline}\nSTATUS: {status} \nSTDOUT: {out.decode().rstrip()} \nSTDERR:{err.decode().rstrip()}")
         root.update()
         root.deiconify()
         return
   root.destroy()
   sys.exit(0)
   
def readdirs(top):
   browsers = []
   bnames = [d for d in os.listdir(top) if os.path.isdir(os.path.join(top, d))]
   bnames.sort()
   for b in bnames:
      bl = browserlist()
      bl.name = b
      bdir = os.path.join(top, b)
      bl.list = [d for d in os.listdir(bdir) if os.path.isdir(os.path.join(bdir, d))]
      bl.list.sort()
      browsers.append(bl)
   return browsers

#if user asks this to be a gui, generate popup menus to select which to launch
def buildgui(basedir, browsers):
   root = tk.Tk()
   windowstype = root.tk.call('tk', 'windowingsystem')     # returns x11, win32 or aqua
   root.geometry("200x1")
   root.title('run browser')
   menubar = tk.Menu(root)
   root.config(menu=menubar)
   b_menu = tk.Menu(menubar)
   menubar.add_cascade(label="browsers", menu=b_menu)
   menubar.add_command(label='Exit', command=root.destroy)
   brm_kep = []  #list of browser cascade menus
   brm_era = []  #list of browser cascade menus
   for b in browsers:
      brm_kep.append(tk.Menu(menubar))
      brm_era.append(tk.Menu(menubar))
      b_menu.add_cascade(label=b.name, menu=brm_kep[len(brm_kep)-1] )
      for p in b.list:
         brm_kep[len(brm_kep)-1].add_command(label=p, command=lambda thisb = b.name, thisp = p: launch(root, basedir, thisb, thisp, "keep"))
         brm_era[len(brm_kep)-1].add_command(label=p, command=lambda thisb = b.name, thisp = p: launch(root, basedir, thisb, thisp, "erase"))
      brm_kep[len(brm_kep)-1].add_command(label="create new", command=lambda thisb = b.name: new_browser(root, basedir, thisb))
      if len(b.list) > 0:
         brm_kep[len(brm_kep)-1].add_cascade(label="delete profile and start", menu=brm_era[len(brm_era)-1])
   root.after(100, lambda: check_for_int(root))
   try:
      root.mainloop()
   except:
      sys.exit(0)


#if user asks for fvwm menu for piperead, print them out
#BROWSERMenu
#  BRM_browsername
#    list of names
#  BRM_browsername
#  BRM_browsername
def fvwmmenu(basedir, browsers):
   print("DestroyModuleConfig  FvwmForm-BrowserProfile: *")
   print("*FvwmForm-BrowserProfile: WarpPointer")
   print("*FvwmForm-BrowserProfile: Line         center")
   print("*FvwmForm-BrowserProfile: Text         \"create new browser profile\"")
   print("*FvwmForm-BrowserProfile: Line         center")
   print("*FvwmForm-BrowserProfile: Text         \"Browser: $(BROWSER)\"")
   print("*FvwmForm-BrowserProfile: Line         center")
   print("*FvwmForm-BrowserProfile: Text         \"Profile:\"")
   print("*FvwmForm-BrowserProfile: Input        BRM_Profile        20      \"\"")
#   print("*FvwmFormBrowserProfile: Button       quit    \"Login\"         ^M")
   print("*FvwmForm-BrowserProfile: Command      LaunchWeb $(BROWSER) $(BRM_Profile) keep")
   #print("*FvwmForm-BrowserProfile: Command      Exec exec ssh $(Custom?-l $(UserName)) $(HostName) xterm -T x")
#   print("DestroyFunction BRM_NewProfile")
#   print("AddToFunction BRM_NewProfile")
#   print("+ I setEnv BRM_BrowserName $0")
#   print("+ I Module FvwmForm BrowserProfile")
   print("DestroyMenu \"BrowserMenu\"")
   print("AddToyMenu \"BrowserMenu\" \"Browsers\" Title")
   for b in browsers:
      popupname = "BRM_"+b.name+"_keep"
      print(f"+ \"{b.name}\" Popup \"{popupname}\"")
   print()
   # make main menus
   for b in browsers:
      popupname = "BRM_"+b.name+"_keep"
      print(f"DestroyMenu \"{popupname}\"")
      print(f"AddToMenu \"{popupname}\" \"{b.name}\" Title")
      for p in b.list:
         print(f"+ \"{p}\" Exec Exec LaunchWeb {b.name} \"{p}\" keep") #TODO: finish this
      print(f"+ \"With New Profile\" Popup \"BRM_{b.name}_erase\" ")
   # make erase menus, same as main but with erase in place of keep
   # TODO: eventually make keep or erase a parameter
   for b in browsers:
      popupname = "BRM_"+b.name+"_erase"
      print(f"DestroyMenu \"{popupname}\"")
      print(f"AddToMenu \"{popupname}\" \"{b.name}\" Title")
      for p in b.list:
         print(f"+ \"{p}\" Exec Exec LaunchWeb {b.name} \"{p}\" erase") #TODO: finish this
      print("+ \"New\" Module FvwmForm BROWSER=b.name")
            
#main
def main():
   p = argparse.ArgumentParser(
          prog='generate-browsermenu.py',
          description='make a menu to select a browser to run')
   p.add_argument('-f', '--fvwm', action='store_true')
   p.add_argument('path', nargs='?', default=DEFAULTPATH)
   args = p.parse_args()
   if not os.path.isdir(args.path):
      p.error(f"path \"{args.path}\" is not a directory")
   browsers=readdirs(args.path)

   if args.fvwm:
      fvwmmenu(args.path, browsers)
   else:
      buildgui(args.path, browsers)


main()
