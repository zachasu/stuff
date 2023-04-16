from apifunctions import *
from dataclasses import dataclass

def to_int(list):
  intlist = []
  for i in list:
    intlist.append(int(i))
  return intlist

def list_to_object(list):
  obj_list = []
  for i in range(len(list)):
    if list[i] in allweapons:
      obj_list.append(allweapons[list[i]])
    elif list[i] in allarmor:
      obj_list.append(allarmor[list[i]])
    elif list[i] in allitems:
      obj_list.append(allitems[list[i]])
    elif list[i] in alleffects:
      obj_list.append(alleffects[list[i]])
    else:
      print("I dunno man " + list[i])
  return obj_list

def to_object(input):
  object = 0
  if input in allweapons:
    object = allweapons[input]
  if input in allarmor:
    object = allarmor[input]
  if input in allitems:
    object = allitems[input]
  if input in alleffects:
    object = alleffects[input]
  return object

#All information here except for stats are lists of strings
#Meaning that I need to to_object() later in the code
class Character:
  def __init__(self, stats, inventory_names, inventory_nums):
    self.stats = stats
    self.health = to_int([stats[0], stats[1]]) #Max, Current
    self.combatstats = to_int([stats[2], stats[3], stats[4]]) #MOV, PROT, WARD
    self.basestats = to_int([stats[5], stats[6], stats[7], stats[8]]) #STR, DEX, INT, FAI
    self.inventory_names = inventory_names
    self.inventory_nums = inventory_nums
    self.inventory_objects = list_to_object(inventory_names)

@dataclass
class Weapon:
  name: str
  spd: str
  dmg: str
  stances: list
  desc: str

@dataclass
class Armor:
  name: str
  mov: str
  effect: str

@dataclass
class Item:
  name: str
  desc: str
  effect: str
  type: str

@dataclass
class Spell:
  name: str
  cost: str
  desc: str

@dataclass
class Effect:
  name: str
  change: str
  amount: str
  desc: str

#Dictionary Definitions
allweapons = {
  "weapon" : Weapon("test_weapon", '1', '2', ['stance1', 'stance2'], "description")
}

allarmor = {
  "armor" : Armor("test_armor", '3', "effect")
}

allitems = {
  "item1" : Item("test_item1", "description", "effect", "consumable"),
  "item2" : Item("test_item2", "description", "effect", "trinket"),
  "item3" : Item("test_item3", "description", "effect", "trinket")
}

alleffects = {
  "Poisoned" : Effect("Poisoned", "damage", 1, "Per Stack, lose 1 STA.")
}

alldicts = {}
alldicts.update(allweapons)
alldicts.update(allarmor)
alldicts.update(allitems)
alldicts.update(alleffects)
