#Autofill Entry Box
import tkinter as tk

root = tk.Tk()
#root.geometry("900x500")

names = ["Dorian", "Davian", "Dave", "Davido"]

def on_keyrelease(names):
  current_input = entry.get().lower()
  matching_names = [name for name in names if name.lower().startswith(current_input)]
  if len(matching_names) == 1:
    entry.delete(0, tk.END)
    entry.insert(0, matching_names[0])

entry = tk.Entry(root)
entry.grid(row=0, column=0)
button = tk.Button(root, text="Button", command=lambda:entry.delete(0, tk.END))
button.grid(row=1, column=0)

entry.bind("<KeyRelease>", lambda event: on_keyrelease(names))

#Open a new window
def open_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is a new window")
    label.pack()

button = tk.Button(root, text="Open New Window", command=open_window)
button.grid(row=0, column=1)

root.mainloop()

