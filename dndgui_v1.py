import tkinter as tk
from ttrpgfunctions import *

width_ = 100
height_ = 70

#These classes are for the GUI displays

#This class is for making displays that show two values comparatively
class Stat1display:
	def __init__ (self, root, label, row_, column_, evalue, svalue):
		self.label=label
		self.evalue=evalue
		self.svalue=svalue
		self.frame=tk.LabelFrame(root, text=label, width=width_, height=height_, padx=15, pady=0)
		self.frame.grid_propagate(False) #disables the auto-shrinking of the frame
		self.frame.grid(row=row_, column=column_, padx=5, pady=0)
		self.entry=tk.Entry(self.frame, width=3)
		self.entry.insert(0, evalue)
		self.entry.grid(row=0, column=0)
		self.label=tk.Label(self.frame, text=svalue, relief="raised", borderwidth=1, width=3, background="#d9d9d9")
		self.label.grid(row=0, column=1)

#This class is for making displays that only show 1 value
class Stat2display:
	def __init__ (self, root, label, row_, column_, real, shown):
		self.label=label
		self.real=real
		self.shown=shown
		self.frame=tk.LabelFrame(root, text=label, width=width_, height=height_, padx=30, pady=0)
		self.frame.grid_propagate(False) #disables the auto-shrinking of the frame
		self.frame.grid(row=row_, column=column_, padx=5, pady=0)
		self.label=tk.Label(self.frame, text=shown, relief="raised", borderwidth=1, width=3, background="#d9d9d9")
		self.label.grid(row=0, column=0)

		#self.entry=tk.Entry(self.frame, width=3)
		#self.entry.insert(0, value1)
		#self.entry.grid(row=0, column=0)

#This class makes the box that displays all of a player's equipment
#Replace all of the weapon and trinket arguments with an Equipment argument
class Equipmentdisplay:
	def __init__ (self, root, row_, column_, equipment):
		self.root=root
		self.equipment=equipment

		self.wframe1=tk.LabelFrame(self.root, text=equipment.weapon1.name, height=height_, width=width_*2)
		self.wframe1.grid_propagate(False)
		self.wframe1.grid(row=row_, column=column_, padx=10)
		self.wframe2=tk.LabelFrame(self.root, text=equipment.weapon2.name, height=height_, width=width_*2)
		self.wframe2.grid_propagate(False)
		self.wframe2.grid(row=row_, column=column_+1, padx=(0,5))
		self.wlabel1=tk.Label(self.wframe1, text="17")
		self.wlabel1.grid(row=0, column=0)
		self.wlabel2=tk.Label(self.wframe2, text="17")
		self.wlabel2.grid(row=0, column=0)

		self.armorframe=tk.LabelFrame(self.root, text=equipment.armor.name, height=height_, width=width_*2)
		self.armorframe.grid_propagate(False)
		self.armorframe.grid(row=row_+1, column=column_, padx=10)
		self.armorlabel=tk.Label(self.armorframe, text="17")
		self.armorlabel.grid(row=0, column=0)

		self.tframe1=tk.LabelFrame(self.root, text=equipment.trinket1.name, height=height_, width=width_*2)
		self.tframe1.grid_propagate(False)
		self.tframe1.grid(row=row_+1, column=column_+1, padx=(0,5))
		self.tlabel1=tk.Label(self.tframe1, text="17")
		self.tlabel1.grid(row=0, column=0)
		self.tframe2=tk.LabelFrame(self.root, text=equipment.trinket2.name, height=height_, width=width_*2)
		self.tframe2.grid_propagate(False)
		self.tframe2.grid(row=row_+2, column=column_+1, padx=(0,5))
		self.tlabel2=tk.Label(self.tframe2, text="17")
		self.tlabel2.grid(row=0, column=0)

#These classes are for organizing information

#Statbonus structure [Str, Dex, Int, Fai]

class Character:
	def __init__ (self, equipment, sta, ap, prot, guard, mov, str, fai, dex, int):
		self.equipment=equipment
		self.sta=sta
		self.ap=ap
		self.prot=prot
		self.guard=guard
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

#Beginning of code

root=tk.Tk()
#root.geometry("700x400")

refresher=tk.Button(root, text="Update")
refresher.grid(row=0, column=2)

sword = Weapon("Sword", 5, 1, 4, "Melee", "", [0, 0, 0, 0])
dagger = Weapon("Dagger", 8, 1, 2, "Melee", "", [0, 0, 0, 0])
tunic = Armor("Tunic", 2, 0, 3, "", [0, 0, 0, 0])
clearstone_ring = Trinket("Clearstone Ring", "On Use: Restore 5 AP", [0, 0, 0, 0])
hunters_guide = Trinket("Hunter's Guide", "On Use: Learn one attribute of a target", [0, 0, 0, 0])

p1equip=Equipment(sword, dagger, tunic, clearstone_ring, hunters_guide)

sta = Stat1display(root, "Stamina", 0, 0, 13, 15)
ap = Stat1display(root, "AP", 1, 0, 13, 15)
prot = Stat2display(root, "Prot", 0, 1, 13, 15)
guard = Stat2display(root, "Guard", 1, 1, 13, 3)
move = Stat2display(root, "Mov", 2, 1, 13, 3)
str = Stat2display(root, "Str", 3, 0, 13, 3)
dex = Stat2display(root, "Dex", 4, 0, 13, 3)
fai = Stat2display(root, "Fai", 3, 1, 13, 3)
int = Stat2display(root, "Int", 4, 1, 13, 3)

equipment = Equipmentdisplay(root, 0, 3, p1equip)

root.mainloop()
