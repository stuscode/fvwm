#!/usr/bin/env python3

import argparse
import os
import tkinter as tk


DEFAULTPATH="~/ssd/browserdirs"

def usage():
   print("generate-browsermenu.py -g|-f [browserdirectory]")
   exit(1)

class browserlist:
   name = ""
   list = []

#get structure of browsers and profiles for each
#browsers = [b1 b2 b3]
#bn = [p1 p2 p3]
   
def readdirs(top):
   browsers = []
   bnames = [d for d in os.listdir(top) if os.path.isdir(os.path.join(top, d))]
   for b in bnames:
      print(b)
      bl = browserlist()
      bl.name = b
      bdir = os.path.join(top, b)
      bl.list = [d for d in os.listdir(bdir) if os.path.isdir(os.path.join(bdir, d))]
      browsers.append(bl)
      print(bl.name, bl.list)
   return browsers

#if user asks this to be a gui, generate popup menus to select which to launch
def buildgui(browsers):
   root = tk.Tk()
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
         brm_kep[len(brm_kep)-1].add_command(label=p)
         brm_era[len(brm_kep)-1].add_command(label=p)
      brm_kep[len(brm_kep)-1].add_command(label="create new")
      if len(b.list) > 0:
         brm_kep[len(brm_kep)-1].add_cascade(label="delete profile and start", menu=brm_era[len(brm_era)-1])
#   file_menu.add_command(label='New')
#   file_menu.add_command(label='Open...')
#   file_menu.add_command(label='Exit', command=root.destroy)
   root.mainloop()


#if user asks for fvwm menu for piperead, print them out
#BROWSERMenu
#  BRM_browsername
#    list of names
#  BRM_browsername
#  BRM_browsername
def fvwmmenu(browsers):
   print("DestroyMenu \"BROWSERMENU\"")
   print("AddToyMenu \"BROWSERMENU\" \"Browsers\" Title")
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
            
#main
def main():
   p = argparse.ArgumentParser(
          prog='generate-browsermenu.py',
          description='make a menu to select a browser to run')
   p.add_argument('-f', '--fvwm', action='store_true')
   p.add_argument('-g', '--gui', action='store_true')
   p.add_argument('path')
   args = p.parse_args()
   print(args)
   if args.fvwm and args.gui:
      p.error("Can only specify one of -f or -g")
   if not args.fvwm and not args.gui:
      p.error("Must specify either -f or -g")
   if not args.path:
      path = DEFAULTPATH
   browsers=readdirs(args.path)

   if args.fvwm:
      fvwmmenu(browsers)
      exit(0)
   if args.gui:
      buildgui(browsers)


main()
