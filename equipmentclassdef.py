import tkinter as tk
from apifunctions import *

class Character:
	def __init__ (self, equipment, stats, inventory):
		self.equipment=equipment
		self.stats=stats
		self.inventory=inventory

		self.cur_sta=stats[0]
		self.max_sta=stats[1]
		self.cur_ap=stats[2]
		self.max_ap=stats[3]
		self.inv=stats[4]
		self.str=stats[5]
		self.dex=stats[6]
		self.int=stats[7]
		self.fai=stats[8]

		self.weapon1=equipment.equipment_list[0]
		self.weapon2=equipment.equipment_list[1]
		self.armor=equipment.equipment_list[2]
		self.trinket1=equipment.equipment_list[3]
		self.trinket2=equipment.equipment_list[4]

		self.bonuses=equipment.sumlist

class Equipment:
	def __init__ (self, equipment_list):
		self.equipment_list=equipment_list
		self.sumlist=[]
		self.statbonus=[]
		for i in range(4): #Store the values in one column of stats and sum them before moving onto the next column
			for j in range(len(equipment_list)):
				self.sumlist.append(equipment_list[j].statbonus[i])
			self.hold=sum(self.sumlist)
			self.statbonus.append(self.hold)
			self.sumlist=[]

class Inventory:
	def __init__(self, inv_data, inv_num):
		self.inv_data=inv_data
		self.inv_num=inv_num

class Weapon:
	def __init__ (self, name, spd, rnge, atk, type, desc, statbonus):
		self.name=name
		self.spd=spd
		self.rnge=rnge
		self.atk=atk
		self.type=type
		self.desc=desc
		self.statbonus=statbonus

class Armor:
	def __init__ (self, name, prot, guard, mov, desc, statbonus):
		self.name=name
		self.prot=prot
		self.guard=guard
		self.mov=mov
		self.desc=desc
		self.statbonus=statbonus

class Trinket:
	def __init__ (self, name, desc, statbonus):
		self.name=name
		self.desc=desc
		self.statbonus=statbonus

class Item:
	def __init__(self, name, desc):
		self.name=name
		self.desc=desc

class Status:
	def __init__(self, name, desc, flat_change, turn_change):
		self.name=name
		self.desc=desc
		self.flat_change=flat_change
		self.turn_change=turn_change

allweapons = {
  "Sword" : Weapon("Sword", 5, 1, 4, "Melee", "", [0, 2, 0, 0]),
  "Dagger" : Weapon("Dagger", 8, 1, 2, "Melee", "", [1, 0, 0, 0])
}

allarmor = {
  "Tunic" : Armor("Tunic", 2, 0, 3, "", [0, 0, 0, 0])
}

alltrinkets = {
  "Clearstone Ring" : Trinket("Clearstone Ring", "On Use: Restore 5 AP", [0, 0, 0, 0]),
  "Hunter's Journal" : Trinket("Hunter's Journal", "On Use: Learn one attribute of a target", [0, 0, 0, 0])
}

allitems = {
  "Potion of Healing" : Item("Potion of Healing", "Heal 5 STA and discard on use")
}
