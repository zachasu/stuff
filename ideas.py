#Equipment Class Nesting Structure
class equipment:
  def __init__ (self, weapon, armor):
    self.weapon = weapon
    self.armor = armor

class weapon:
  def __init__ (self, name, type, speed, range, damage, ability1=None, ability2=None, effect="", statch=[]):
    self.type = type
    self.speed = speed
    self.range = range
    self.damage = damage
    self.fart = 0

class armor:
  def __init__ (self, name, protection, mobility):
    self.protection = protection
    self.mobility = mobility

class ability:
  def __init__ (self, effect, type="", speed=0, range=0, damage=0):
    self.effect = effect

#Autofill Entry Box
import tkinter as tk

root = tk.Tk()
root.geometry("900x500")

names = ["Dorian", "Davian", "Dave", "Davido"]

def on_keyrelease(names):
  current_input = entry.get().lower()
  matching_names = [name for name in names if name.lower().startswith(current_input)]
  if len(matching_names) == 1:
    entry.delete(0, tk.END)
    entry.insert(0, matching_names[0])

entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Button", command=lambda:entry.delete(0, tk.END))
button.pack()

entry.bind("<KeyRelease>", lambda event: on_keyrelease(names))

root.mainloop()

