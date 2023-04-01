import tkinter as tk
from apifunctions import *
from tkinterdisplayclassdef import *

#These classes are for organizing information
#Statbonus structure [Str, Dex, Int, Fai]

allbonus = []
windows = {}

class Character:
	def __init__ (self, equipment, stats, effects, bonuses):
		self.equipment=equipment
		self.currentsta=currentsta
		self.maxsta=maxsta
		self.currentap=currentap
		self.maxap=maxap
		self.prot=prot
		self.currentguard=currentguard
		self.maxguard=maxguard
		self.mov=mov
		self.str=str
		self.fai=fai
		self.dex=dex
		self.int=int

class Equipment:
	def __init__ (self, weapon1, weapon2, armor, trinket1, trinket2):
		self.weapon1=weapon1
		self.weapon2=weapon2
		self.armor=armor
		self.trinket1=trinket1
		self.trinket2=trinket2
		self.statbonus=[]
		for i in range(len(4)):
			statbonus.append(weapon1.statbonus[i]+weapon2.statbonus[i]+armor.statbonus[i]+trinket1.statbonus[i]+trinket2.statbonus[i])

class Weapon:
	def __init__ (self, name, spd, rnge, atk, type, effect, statbonus):
		self.name=name
		self.spd=spd
		self.rnge=rnge
		self.atk=atk
		self.type=type
		self.effect=effect
		self.statbonus=statbonus

class Armor:
	def __init__ (self, name, prot, guard, mov, effect, statbonus):
		self.name=name
		self.prot=prot
		self.guard=guard
		self.mov=mov
		self.effect=effect
		self.statbonus=statbonus

class Trinket:
	def __init__ (self, name, effect, statbonus):
		self.name=name
		self.effect=effect
		self.statbonus=statbonus

#I may need to move these class definitions to another file and import them as this program is getting very long
#I will also need to make another file that acts as a repository for specific items like a sword or a shield

class Windowmanager:
	def __init__ (self, alldata):
		self.alldata=alldata
		self.windows = {}
		sword = Weapon("Sword", 5, 1, 4, "Melee", "", [0, 0, 0, 0])
		dagger = Weapon("Dagger", 8, 1, 2, "Melee", "", [0, 0, 0, 0])
		tunic = Armor("Tunic", 2, 0, 3, "", [0, 0, 0, 0])
		clearstone_ring = Trinket("Clearstone Ring", "On Use: Restore 5 AP", [0, 0, 0, 0])
		hunters_guide = Trinket("Hunter's Guide", "On Use: Learn one attribute of a target", [0, 0, 0, 0])

	def remove_window(self, window_id):
		windows[window_id].destroy()
		del windows[window_id]

	def create_new_window(self, window_id):
		new_window=tk.Toplevel()
		new_window.title(f"window {window_id}")
		new_window.protocol("WM_DELETE_WINDOW", lambda: self.remove_window(window_id))
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

test = Stat1display(root, "test", 0, 0, teb, teb)
testbutton=tk.Button(root, text="test", command=lambda: windowm.on_button_click(1, windowm.create_new_window))
buttontest=tk.Button(root, text="test", command=lambda: windowm.on_button_click(2, windowm.create_new_window))
printbutton=tk.Button(root, text="print", command=lambda: print(windows))
testbutton.grid(row=0, column=0)
buttontest.grid(row=1, column=0)
printbutton.grid(row=2, column=0)

#sta = Stat1display(new_window, "Stamina", 0, 0, 13, 15)
#ap = Stat1display(new_window, "AP", 1, 0, 13, 15)
#prot = Stat2display(new_window, "Prot", 0, 1, 13, 15)
#guard = Stat2display(new_window, "Guard", 1, 1, 13, 3)
#move = Stat2display(new_window, "Mov", 2, 1, 13, 3)
#str = Stat2display(new_window, "Str", 3, 0, 13, 3)
#dex = Stat2display(new_window, "Dex", 4, 0, 13, 3)
#fai = Stat2display(new_window, "Fai", 3, 1, 13, 3)
#int = Stat2display(new_window, "Int", 4, 1, 13, 3)
#weapon1 = Equipmentdisplay(new_window, 0, 0, sword)
#weapon2 = Equipmentdisplay(new_window, 0, 1, dagger)
#armor = Equipmentdisplay(new_window, 1, 0, tunic)
#trinket1 = Equipmentdisplay(new_window, 1, 1, clearstone_ring)
#trinket2 = Equipmentdisplay(new_window, 2, 1, hunters_guide)

root.mainloop()
