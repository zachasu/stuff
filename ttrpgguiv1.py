import tkinter as tk
from apifunctions import *
from equipmentclassdef import *
from tkinterdisplayclassdef import *

#These classes are for organizing information
#Statbonus structure [Str, Dex, Int, Fai]

allbonus = []
windows = {}

#I may need to move these class definitions to another file and import them as this program is getting very long
#I will also need to make another file that acts as a repository for specific items like a sword or a shield

class Windowmanager:
	def __init__ (self, alldata):
		self.alldata=alldata
		self.windows = {}

		self.sword = Weapon("Sword", 5, 1, 4, "Melee", "", [0, 0, 0, 0])
		self.dagger = Weapon("Dagger", 8, 1, 2, "Melee", "", [0, 0, 0, 0])
		self.tunic = Armor("Tunic", 2, 0, 3, "", [0, 0, 0, 0])
		self.clearstone_ring = Trinket("Clearstone Ring", "On Use: Restore 5 AP", [0, 0, 0, 0])
		self.hunters_guide = Trinket("Hunter's Guide", "On Use: Learn one attribute of a target", [0, 0, 0, 0])

	def remove_window(self, window_id):
		windows[window_id].destroy()
		del windows[window_id]

	def create_new_window(self, window_id):
		new_window=tk.Toplevel()
		new_window.title(f"window {window_id}")
		new_window.protocol("WM_DELETE_WINDOW", lambda: self.remove_window(window_id))
		return new_window

	def create_stat_window(self, window_id):
		new_window=tk.Toplevel()
		new_window.title(f"window {window_id}")
		new_window.protocol("WM_DELETE_WINDOW", lambda: self.remove_window(window_id))
		sta = Stat1display(new_window, "Stamina", 0, 0, 13, 15)
		ap = Stat1display(new_window, "AP", 1, 0, 13, 15)
		prot = Stat2display(new_window, "Prot", 0, 1, 13, 15)
		guard = Stat2display(new_window, "Guard", 1, 1, 13, 3)
		move = Stat2display(new_window, "Mov", 2, 1, 13, 3)
		str = Stat2display(new_window, "Str", 3, 0, 13, 3)
		dex = Stat2display(new_window, "Dex", 4, 0, 13, 3)
		fai = Stat2display(new_window, "Fai", 3, 1, 13, 3)
		int = Stat2display(new_window, "Int", 4, 1, 13, 3)
		return new_window

	def create_equip_window(self, window_id):
		new_window=tk.Toplevel()
		new_window.title(f"window {window_id}")
		new_window.protocol("WM_DELETE_WINDOW", lambda: self.remove_window(window_id))
		weapon1 = Equipmentdisplay(new_window, 0, 0, sword)
		weapon2 = Equipmentdisplay(new_window, 0, 1, dagger)
		armor = Equipmentdisplay(new_window, 1, 0, tunic)
		trinket1 = Equipmentdisplay(new_window, 1, 1, clearstone_ring)
		trinket2 = Equipmentdisplay(new_window, 2, 1, hunters_guide)
		return new_window

	def on_button_click(self, window_id, func):
		if window_id in windows:
			window = windows[window_id]
			if window.winfo_exists():
				window.lift()
				print(windows)
			else:
				windows[window_id]=func(window_id)
		else:
			windows[window_id]=func(window_id)

#Beginning of code

#Make DICTIONARIES that use Strings to point at the Objects they apply to {'sword' : sword}
alldata = getValues('A1:K')
stats = alldata[0]
equipment = alldata[1]
inventory = alldata[2]
root=tk.Tk()
root.geometry("700x400")
windowm = Windowmanager(alldata)

statbutton=tk.Button(root, text="Stats", command=lambda: windowm.on_button_click(1, windowm.create_stat_window))
equipbutton=tk.Button(root, text="Equipment", command=lambda: windowm.on_button_click(2, windowm.create_equip_window))
printbutton=tk.Button(root, text="print windows{}", command=lambda: print(windows))
statbutton.grid(row=0, column=0)
equipbutton.grid(row=1, column=0)
printbutton.grid(row=2, column=0)

sword = Weapon("Sword", 5, 1, 4, "Melee", "", [0, 0, 0, 0])
dagger = Weapon("Dagger", 8, 1, 2, "Melee", "", [0, 0, 0, 0])
tunic = Armor("Tunic", 2, 0, 3, "", [0, 0, 0, 0])
clearstone_ring = Trinket("Clearstone Ring", "On Use: Restore 5 AP", [0, 0, 0, 0])
hunters_guide = Trinket("Hunter's Guide", "On Use: Learn one attribute of a target", [0, 0, 0, 0])

root.mainloop()
