#Autofill Entry Box
import tkinter as tk
from tkinter import ttk

#root = tk.Tk()
#root.geometry("900x500")

##Autofill
#names = ["Dorian", "Davian", "Dave", "Davido"]
#
#def on_keyrelease(names):
#  current_input = entry.get().lower()
#  matching_names = [name for name in names if name.lower().startswith(current_input)]
#  if len(matching_names) == 1:
#    entry.delete(0, tk.END)
#    entry.insert(0, matching_names[0])
# 
#if __name__ == '__main__':
#  entry = tk.Entry(root)
#  entry.grid(row=0, column=0)
#  button = tk.Button(root, text="Button", command=lambda:entry.delete(0, tk.END))
#  button.grid(row=1, column=0)
#
#  entry.bind("<KeyRelease>", lambda event: on_keyrelease(names))
#
##Open a new window
#def open_window():
#    new_window = tk.Toplevel(root)
#    new_window.title("New Window")
#    label = tk.Label(new_window, text="This is a new window")
#    label.pack()
#
#if __name__ == '__main__':
#  button1 = tk.Button(root, text="Open New Window", command=open_window)
#  button1.grid(row=0, column=1)

class App:
  def __init__(self, master):
      self.master = master
      self.master.title("Progress Bar Example")
      
      self.value = tk.StringVar()
      self.value.set("50")
       
      self.entry = tk.Entry(self.master, textvariable=self.value)
      self.entry.pack(fill=tk.X, padx=10, pady=10)
        
      self.progress = tk.ttk.Progressbar(self.master, orient=tk.HORIZONTAL, mode='determinate', maximum = 15)
      self.progress.pack(fill=tk.X, padx=10, pady=10)

      self.progress_label = ttk.Label(self.master, text='50%')
      self.progress_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
      self.update_bar()
        
      self.value.trace("w", self.update_bar)
        
  def update_bar(self, *args):
      try:
          val = int(self.value.get())
      except ValueError:
          val = 0
      
      if val < 0:
          val = 0
      elif val > 15:
          val = 15
      
      self.progress["value"] = val
        
if __name__ == '__main__':
  root = tk.Tk()
  app = App(root)
  root.mainloop()

