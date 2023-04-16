import tkinter as tk
from apifunctions import *
from equipmentclassdef2 import *
from guidisplayfunctions import *

def on_entry_click(entry, text):
  if entry.get() == text:
    entry.delete(0, tk.END)
    entry.insert(0, '')
    entry.config(fg = 'black')

def on_entry_leave(entry, text):
  if len(entry.get()) == 0:
    entry.insert(0, text)
    entry.config(fg = 'grey')

def main(range):
  range1 = str(((int(range)-1)*10)+1)
  range2 = str(int(range)*10)
  print(range1)
  print(range2)
  if len(range) == 1:
    for i in root.winfo_children():
      i.destroy()
    alldata = getValues('A' + (range1) + ':J' + (range2))
    character = Character(alldata[0], alldata[1], alldata[2])
    windowm = Windowmanager(character, root)

root = tk.Tk()
root.option_add("*Font", "TkDefaultFont 10")
root.geometry("1200x700")

nam_ent = tk.Entry(root, width = 13, fg='grey')
nam_ent.insert(0, 'Player Number')
nam_ent.bind('<FocusIn>', lambda event: on_entry_click(nam_ent, 'Player Number'))
nam_ent.bind('<FocusOut>', lambda event: on_entry_leave(nam_ent, 'Player Number'))
nam_ent.grid(row=0, column=0)
confirm = tk.Button(root, text = 'Confirm')
confirm.config(command = lambda: main(nam_ent.get()))
confirm.grid(row=0, column=1)

root.mainloop()
