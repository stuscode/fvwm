#!/usr/bin/env python3

import tkinter

root = tkinter.Tk()
with open("/main/SyncDir/public/aaaa.txt", 'w') as out:
   out.write(root.selection_get(selection="PRIMARY"))
#print("primary:", root.selection_get(selection="PRIMARY"))
#print("clipboard:", root.selection_get(selection="CLIPBOARD"))
#root.clipboard_clear()
#root.clipboard_append("Your text here")
#root.mainloop()
