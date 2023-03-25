import tkinter as tk
from ttrpgfunctions import *

window=tk.Tk()

window.title('Testing Window')
window.geometry("900x500")

class comp_display:
  def __init__ (self, label, root, row, column):
    self.label = label
    self.root = root
    self.frame1 = tk.LabelFrame(root, text=label, pady=5, padx=5, height=88, width=120, borderwidth=0, highlightthickness=0)
    self.frame2 = tk.Frame(root, pady=5, padx=5)
    self.label1 = tk.Label(frame1, text='null', width=5, height=2, font=('Arial', 20))
    self.label2 = tk.Label(frame1, text='null', width=5, height=2, font=('Arial', 20))
    self.button1 = tk.Button(frame2, text='+', width=1, height=1)
    self.button2 = tk.Button(frame2, text='-', width=1, height=1)

  def setup (self, position, function, function2)
    self.button1.config(command=lambda:function)
    self.button2.config(command=lambda:function2)
    self.frame1.grid(row=position, column=position)
    self.frame1.grid_propagate(False)
    self.frame2.grid(row=position, column=position+1)
    self.frame2.grid_propagate(False)

gray1 = '#808080'
gray2 = '#A9A9A9'

sta_display = tk.LabelFrame(window, text="Stamina", pady=5, padx=5, height=88, width=120)
sta_display.configure(bg=gray2, borderwidth=0, highlightthickness=0)
sta_display.grid(row=0, column=0)
sta_display.grid_propagate(False)

sta_button = tk.Frame(window)
sta_button.configure(bg=gray1, pady=5, padx=5, height=10) 
sta_button.grid(row=0, column=1)
sta_button.grid_propagate(False)

sta_cur=tk.Label(sta_display, text=17, width=5, height=2, font=('Arial', 20))
sta_cur.grid(row=0, column=0, padx=(0,5))
sta_total=tk.Label(sta_display, text=27, width=5, height=2, font=('Arial', 20))
sta_total.grid(row=0, column=1)

sta_display.grid_rowconfigure(0, weight=1)
sta_display.grid_columnconfigure(0, weight=1)
sta_display.grid_columnconfigure(1, weight=1)

button = tk.Button(sta_button, text="+", width=1, height=1, command=lambda:print(getValues(range)))
button.grid_propagate(False)
button.pack()
button2 = tk.Button(sta_button, text="-", width=1, height=1, command=lambda:sendUpdate(range, [[a1,a2],[b1,b2]]))
button2.grid_propagate(False)
button2.pack()

window.mainloop()

#sendUpdate('A1', [[2,2],[4,4]])
print(getValues('A1:B2')[0][0])
