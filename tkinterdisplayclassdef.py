import tkinter as tk
from apifunctions import *
from equipmentclassdef import *

width_ = 100
height_ = 70

#These classes are for the GUI displays

#This class is for making displays that show two values comparatively
class Stat1display:
	def __init__ (self, root, label, row_, column_, evalue, svalue):
		self.label=label
		self.evalue=evalue
		self.svalue=svalue
		self.row_=row_
		self.column_=column_
		self.frame=tk.LabelFrame(root, text=label, width=width_, height=height_, padx=15, pady=10)
		self.entry=tk.Entry(self.frame, width=3)
		self.entry.insert(0, evalue)
		self.label=tk.Label(self.frame, text=svalue, relief="raised", borderwidth=1, width=3, background="#d9d9d9")
		self.frame.grid(row=self.row_, column=self.column_, padx=5, pady=0)
		self.entry.grid(row=0, column=0)
		self.label.grid(row=0, column=1)

#This class is for making displays that only show 1 value
class Stat2display:
	def __init__ (self, root, label, row_, column_, real, shown):
		self.label=label
		self.real=real
		self.shown=shown
		self.row_=row_
		self.column_=column_
		self.frame=tk.LabelFrame(root, text=label, width=width_, height=height_, padx=30, pady=10)
		self.label=tk.Label(self.frame, text=shown, relief="raised", borderwidth=1, width=3, background="#d9d9d9")
		self.frame.grid(row=self.row_, column=self.column_, padx=5, pady=0)
		self.label.grid(row=0, column=0)

#This class makes the box that displays all of a player's equipment
#Replace all of the weapon and trinket arguments with an Equipment argument
class Equipmentdisplay:
	def __init__ (self, root, row_, column_, equipment):
		self.root=root
		self.equipment=equipment
		self.row_=row_
		self.column_=column_

		if isinstance(self.equipment, Weapon):
			self.frame=tk.Frame(self.root, padx=5, pady=5)
			self.frame.grid(row=row_, column=column_)
			self.entrybox=tk.Entry(self.frame)
			self.entrybox.insert(0, equipment.name)
			self.tag1=tk.Label(self.frame, text="SPD", width=3, font=('', 8))
			self.tag2=tk.Label(self.frame, text="RGE", width=3, font=('', 8))
			self.tag3=tk.Label(self.frame, text="DMG", width=3, font=('', 8))
			self.label1=tk.Label(self.frame, text=equipment.spd, width=3)
			self.label2=tk.Label(self.frame, text=equipment.rnge, width=3)
			self.label3=tk.Label(self.frame, text=equipment.atk, width=3)
			if len(equipment.desc) > 0:
				self.effect=tk.Label(self.frame, text=equipment.desc, wraplength=220)
				self.effect.grid(row=1, column=0, columnspan=3, sticky="W")
			self.entrybox.grid(row=0, column=0, columnspan=3, sticky="W")
			self.tag1.grid(row=1, column=0)
			self.tag2.grid(row=1, column=1)
			self.tag3.grid(row=1, column=2)
			self.label1.grid(row=2, column=0)
			self.label2.grid(row=2, column=1)
			self.label3.grid(row=2, column=2)

		elif isinstance(self.equipment, Armor):
			self.frame=tk.Frame(self.root, padx=5, pady=5)
			self.frame.grid(row=row_, column=column_)
			self.entrybox=tk.Entry(self.frame)
			self.entrybox.insert(0, equipment.name)
			self.tag1=tk.Label(self.frame, text="PRT", width=3, font=('', 8))
			self.tag2=tk.Label(self.frame, text="GRD", width=3, font=('', 8))
			self.tag3=tk.Label(self.frame, text="MOV", width=3, font=('', 8))
			self.label1=tk.Label(self.frame, text=equipment.prot, width=3)
			self.label2=tk.Label(self.frame, text=equipment.guard, width=3)
			self.label3=tk.Label(self.frame, text=equipment.mov, width=3)
			if len(equipment.desc) > 0:
				self.effect=tk.Label(self.frame, text=equipment.desc, wraplength=220)
				self.effect.grid(row=1, column=0, columnspan=3, sticky="W")
			self.entrybox.grid(row=0, column=0, columnspan=3, sticky="W")
			self.tag1.grid(row=1, column=0)
			self.tag2.grid(row=1, column=1)
			self.tag3.grid(row=1, column=2)
			self.label1.grid(row=2, column=0)
			self.label2.grid(row=2, column=1)
			self.label3.grid(row=2, column=2)

		elif isinstance(self.equipment, Trinket):
			self.frame=tk.Frame(self.root, padx=5, pady=5)
			self.frame.grid(row=row_, column=column_)
			self.entrybox=tk.Entry(self.frame)
			self.entrybox.insert(0, equipment.name)
			self.effect=tk.Label(self.frame, text=equipment.desc, wraplength=220)
			self.entrybox.grid(row=0, column=0, columnspan=3, sticky="W")
			self.effect.grid(row=1, column=0, columnspan=3, sticky="W")

		else:
			print(isinstance(self.equipment, Weapon))
			print(type(self.equipment))

class Inventorydisplay:
	def __init__(self, root, row_, column_, item, item_num):
		self.root=root
		self.row_=row_
		self.column_=column_
		self.item=item
		self.frame=tk.Frame(self.root, padx=5, pady=5)
		self.frame.grid(row=row_, column=column_, sticky="NW")
		self.nameentry=tk.Entry(self.frame)
		self.numentry=tk.Entry(self.frame, width=3)
		self.nameentry.grid(row=0, column=0)
		self.numentry.grid(row=0, column=1)
		if item != '':
			self.nameentry.insert(0, item.name)
			self.numentry.insert(0, item_num)
			self.itemdesc=tk.Label(self.frame, text="Effect: " + item.desc, wraplength=200)
			self.itemdesc.grid(row=1, column=0, columnspan=2, sticky="NW")
