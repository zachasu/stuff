import tkinter as tk
from apifunctions import *
from equipmentclassdef import *
from tkinterdisplayclassdef import *

allbonus = []
windows = {}

class Windowmanager:
	def __init__ (self, character):
		self.windows = {}
		self.character=character
		self.stats=character.stats
		self.equipment=character.equipment
		self.inventory=character.inventory

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
		sta = Stat1display(new_window, "Stamina", 0, 0, self.stats[0], self.stats[1])
		ap = Stat1display(new_window, "AP", 1, 0, self.stats[2], self.stats[3])
		prot = Stat2display(new_window, "Prot", 0, 1, self.equipment.equipment_list[2].prot, self.equipment.equipment_list[2].prot)
		guard = Stat2display(new_window, "Guard", 1, 1, self.equipment.equipment_list[2].guard, self.equipment.equipment_list[2].guard)
		move = Stat2display(new_window, "Mov", 2, 1, self.equipment.equipment_list[2].mov, self.equipment.equipment_list[2].mov)
		str = Stat2display(new_window, "Str", 3, 0, self.stats[5], self.stats[5])
		dex = Stat2display(new_window, "Dex", 4, 0, self.stats[6], self.stats[6])
		fai = Stat2display(new_window, "Fai", 3, 1, self.stats[7], self.stats[7])
		int = Stat2display(new_window, "Int", 4, 1, self.stats[8], self.stats[8])
		return new_window

	def create_equip_window(self, window_id):
		new_window=tk.Toplevel()
		new_window.title(f"window {window_id}")
		new_window.protocol("WM_DELETE_WINDOW", lambda: self.remove_window(window_id))
		weapon1 = Equipmentdisplay(new_window, 0, 0, self.equipment.equipment_list[0])
		weapon2 = Equipmentdisplay(new_window, 0, 1, self.equipment.equipment_list[1])
		armor = Equipmentdisplay(new_window, 1, 0, self.equipment.equipment_list[2])
		trinket1 = Equipmentdisplay(new_window, 1, 1, self.equipment.equipment_list[3])
		trinket2 = Equipmentdisplay(new_window, 2, 1, self.equipment.equipment_list[4])
		return new_window

	def create_inv_window(self, window_id):
		new_window=tk.Toplevel()
		new_window.title(f"window {window_id}")
		new_window.protocol("WM_DELETE_WINDOW", lambda: self.remove_window(window_id))
		for i in range (6+self.stats[4]):
			if i < len(self.inventory.inv_data):
				inv = Inventorydisplay(new_window, i//2, i%2, self.inventory.inv_data[i], self.inventory.inv_num[i])
			else:
				inv = Inventorydisplay(new_window, i//2, i%2, '', 0)
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

def to_object(data_list):
	obj_list = []
	for i in range(len(data_list)):
		if data_list[i] in allweapons:
			obj_list.append(allweapons[data_list[i]])
		elif data_list[i] in allarmor:
			obj_list.append(allarmor[data_list[i]])
		elif data_list[i] in alltrinkets:
			obj_list.append(alltrinkets[data_list[i]])
		elif data_list[i] in allitems:
			obj_list.append(allitems[data_list[i]])
		else:
			print("I dunno man")
	return obj_list

#Beginning of code

alldata = getValues('A1:K')

raw_stats = alldata[0]
stats = list(map(int, raw_stats))

raw_equipment = alldata[1]
object_equipment = to_object(raw_equipment)

raw_inventory = alldata[2]
object_inventory = to_object(raw_inventory)

raw_inventory_amounts = alldata[3]
inventory_amounts = list(map(int, raw_inventory_amounts))

charEquipment = Equipment(object_equipment)
charInventory = Inventory(object_inventory, inventory_amounts)
character = Character(charEquipment, stats, charInventory)

root=tk.Tk()
windowm = Windowmanager(character)

statbutton=tk.Button(root, text="Stats", command=lambda: windowm.on_button_click(1, windowm.create_stat_window))
equipbutton=tk.Button(root, text="Equipment", command=lambda: windowm.on_button_click(2, windowm.create_equip_window))
printbutton=tk.Button(root, text="print windows{}", command=lambda: print(windows))
invbutton=tk.Button(root, text="Inventory", command=lambda: windowm.on_button_click(3, windowm.create_inv_window))
statbutton.grid(row=0, column=0)
equipbutton.grid(row=1, column=0)
invbutton.grid(row=2, column=0)
printbutton.grid(row=3, column=0)

#print(stats)
#print(type(stats[0]))
#for i in range(len(object_equipment)):
#	print(object_equipment[i].name)

root.mainloop()
