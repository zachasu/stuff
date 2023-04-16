import tkinter as tk
from equipmentclassdef2 import *
from tkinter import ttk
import math

def on_entry_click(entry, text):
  if entry.get() == text:
    entry.delete(0, tk.END)
    entry.insert(0, '')
    entry.config(fg = 'black')

def on_entry_leave(entry, text):
  if len(entry.get()) == 0:
    entry.insert(0, text)
    entry.config(fg = 'grey')

class Windowmanager:
  def __init__(self, character, root):
    self.character = character
    self.root = root

    self.nametag = tk.Label(root, text="Name: ", padx=10, pady=10, relief='raised', borderwidth=2)
    self.nametag.grid(row=0, column=0, columnspan=10, sticky='w', padx=10, pady=10)

    self.max_health = tk.IntVar()
    self.max_health.set(self.character.health[0])
    self.current_health = tk.IntVar()
    self.current_health.set(self.character.health[1])

    self.mov = tk.IntVar()
    self.mov.set(self.character.combatstats[0])
    self.prot = tk.IntVar()
    self.prot.set(self.character.combatstats[1])
    self.ward = tk.IntVar()
    self.ward.set(self.character.combatstats[2])

    self.str = tk.IntVar()
    self.str.set(self.character.basestats[0])
    self.dex = tk.IntVar()
    self.dex.set(self.character.basestats[1])
    self.int = tk.IntVar()
    self.int.set(self.character.basestats[2])
    self.fai = tk.IntVar()
    self.fai.set(self.character.basestats[3])

    self.drawDefenseWindow()
    self.drawDamageWindow()
    self.drawStatWindow()
    self.drawEquipWindow()
    self.drawInventoryWindow()
     
  def drawDefenseWindow(self):
    self.defFrame = tk.Frame(self.root, relief='raised', borderwidth=2, padx=10, pady=10)
    self.defFrame.grid(row=1, column=0, padx=10, pady=(0,10), sticky='nw')

    self.label = tk.Label(self.defFrame, text='STA:')
    self.label.grid(row=0, column=0, sticky='w')
    self.health_ntry = tk.Entry(self.defFrame, textvariable=self.current_health, width=3, justify='center')
    self.health_ntry.grid(row=0, column=1, sticky='w')
        
    self.healthbar = tk.ttk.Progressbar(self.defFrame, orient=tk.HORIZONTAL, mode='determinate', maximum=15, length=200)
    self.healthbar.grid(row=1, column=0, columnspan=4)

    self.label = tk.Label(self.defFrame, text='PROT:')
    self.label.grid(row=2, column=0, sticky='w')
    self.prot_ntry = tk.Entry(self.defFrame, textvariable=self.prot, width=3, justify='center')
    self.prot_ntry.grid(row=2, column=1, sticky='w')

    self.label = tk.Label(self.defFrame, text='WARD:')
    self.label.grid(row=2, column=2, sticky='w')
    self.ward_ntry = tk.Entry(self.defFrame, textvariable=self.ward, width=3, justify='center')
    self.ward_ntry.grid(row=2, column=3, sticky='w')
        
    self.update_bar()
    self.current_health.trace("w", self.update_bar)

  def update_bar(self, *args):
    try:
        val = int(self.current_health.get())
    except ValueError:
        val = 0
      
    if val < 0:
        val = 0
    elif val > 15:
        val = 15
        
    self.healthbar["value"] = val

  def drawDamageWindow(self):
    self.damageFrame = tk.Frame(self.root, relief='raised', borderwidth=2, padx=10, pady=10)
    self.damageFrame.grid(row=1, column=1, pady=(0,10), sticky='nw')

    self.label = tk.Label(self.damageFrame, text='DMG:')
    self.label.grid(row=0, column=0)

    self.dmg_ntry = tk.Entry(self.damageFrame, width=5, justify='center')
    self.dmg_ntry.grid(row=0, column=1, pady=4)

    self.phy_button = tk.Button(self.damageFrame, width=3, text='PHY', command=lambda: self.dealDamage(self.prot))
    self.phy_button.grid(row=1, column=0)

    self.mgk_button = tk.Button(self.damageFrame, width=3, text='MGK', command=lambda: self.dealDamage(self.ward))
    self.mgk_button.grid(row=1, column=1)

  def dealDamage(self, intvar):
    intvar.set(intvar.get() - int(self.dmg_ntry.get()))
    if intvar.get() < 0:
      self.current_health.set(self.current_health.get() + intvar.get())
      if self.current_health.get() < 0:
        self.current_health.set(0)
      intvar.set(0)

  def drawStatWindow(self):
    self.statFrame = tk.Frame(self.root, relief='raised', borderwidth=2, padx=10, pady=10)
    self.statFrame.grid(row=2, column=0, sticky='nw', padx=(10,0))

    self.label = tk.Label(self.statFrame, text='STR:')
    self.label.grid(row=0, column=0, pady=(0,10))
    self.str_ntry = tk.Entry(self.statFrame, textvariable=self.str, width=3, justify='center')
    self.str_ntry.grid(row=0, column=1, padx=(0,10), pady=(0,10))

    self.label = tk.Label(self.statFrame, text='DEX:')
    self.label.grid(row=0, column=2, pady=(0,10))
    self.dex_ntry = tk.Entry(self.statFrame, textvariable=self.dex, width=3, justify='center')
    self.dex_ntry.grid(row=0, column=3, padx=(0,10), pady=(0,10))

    self.label = tk.Label(self.statFrame, text='INT:')
    self.label.grid(row=1, column=0)
    self.int_ntry = tk.Entry(self.statFrame, textvariable=self.int, width=3, justify='center')
    self.int_ntry.grid(row=1, column=1, padx=(0,10))

    self.label = tk.Label(self.statFrame, text='FAI:')
    self.label.grid(row=1, column=2)
    self.fai_ntry = tk.Entry(self.statFrame, textvariable=self.fai, width=3, justify='center')
    self.fai_ntry.grid(row=1, column=3, padx=(0,10))

  def drawEquipWindow(self):
    self.equipFrame = tk.Frame(self.root, relief='raised', borderwidth=2, padx=10, pady=10)
    self.equipFrame.grid(row=3, column=0, sticky='nw', columnspan=3, pady=10, padx=10)

    self.weaponFrame = tk.Frame(self.equipFrame)
    self.weaponFrame.grid(row=0, column=0, sticky='nw')
    self.weapon_ntry = tk.Entry(self.weaponFrame, width=10)
    self.weapon_ntry.grid(row=0, column=0, sticky='nw')
    self.weapon_ntry.bind("<KeyRelease>", lambda event: self.equipment_search(allweapons, self.weapon_ntry))
    self.weaponDesc = tk.Label(self.weaponFrame, text='WEAPON', justify='left', wraplength=150)
    self.weaponDesc.grid(row=1, column=0)

    self.armorFrame = tk.Frame(self.equipFrame)
    self.armorFrame.grid(row=0, column=1, sticky='nw')
    self.armor_ntry = tk.Entry(self.armorFrame, width=10)
    self.armor_ntry.grid(row=0, column=0, sticky='nw')
    self.armor_ntry.bind("<KeyRelease>", lambda event: self.equipment_search(allarmor, self.armor_ntry))
    self.armorDesc = tk.Label(self.armorFrame, text='ARMOR', justify='left', wraplength=150)
    self.armorDesc.grid(row=1, column=0)

    self.itemFrame = tk.Frame(self.equipFrame)
    self.itemFrame.grid(row=0, column=2)
    self.item_ntry = tk.Entry(self.itemFrame, width=10)
    self.item_ntry.grid(row=0, column=0)
    self.item_ntry.bind("<KeyRelease>", lambda event: self.equipment_search(allitems, self.item_ntry))
    self.itemDesc = tk.Label(self.itemFrame, text='ITEM', justify='left', wraplength=150)
    self.itemDesc.grid(row=1, column=0)

    self.item_ntry2 = tk.Entry(self.itemFrame, width=10)
    self.item_ntry2.grid(row=2, column=0)
    self.item_ntry2.bind("<KeyRelease>", lambda event: self.equipment_search(allitems, self.item_ntry2))
    self.itemDesc2 = tk.Label(self.itemFrame, text='ITEM', justify='left', wraplength=150)
    self.itemDesc2.grid(row=3, column=0)

  def equipment_search(self, list, entry):
    current_input = entry.get().lower()
    matching_names = [x for x in list if x.lower().startswith(current_input)]
    print(type(matching_names))

    if len(matching_names) == 1:
      entry.delete(0, tk.END)
      entry.insert(0, matching_names[0])
      if isinstance(to_object(matching_names[0]), Weapon):
        result = 'SPD: ' + allweapons[matching_names[0]].spd + '/ DMG: ' + allweapons[matching_names[0]].dmg + '\n STANCES: '
        for i in allweapons[matching_names[0]].stances:
          result += i.upper() + ' ' 
        self.weaponDesc.config(text=result)

      elif isinstance(to_object(matching_names[0]), Armor):
        result = 'MOV: ' + allarmor[matching_names[0]].mov + '\n EFFECT: ' + allarmor[matching_names[0]].effect
        self.armorDesc.config(text=result)

      elif isinstance(to_object(matching_names[0]), Item):
        result = 'TYPE: ' + allitems[matching_names[0]].type + '\n EFFECT: ' + allitems[matching_names[0]].effect
        if entry == self.item_ntry:
          self.itemDesc.config(text=result)
        if entry == self.item_ntry2:
          self.itemDesc2.config(text=result)

  def drawInventoryWindow(self):
    self.invDict = {}
    self.invFrame = tk.Frame(self.root, relief='raised', borderwidth=2, padx=10, pady=10)
    self.invFrame.grid(row=1, column=3, sticky='nw', rowspan=4, pady=0, padx=10)

    for i in range(10):
      inv_ntry = tk.Entry(self.invFrame)
      inv_ntry.pack()
      self.invDict[f'entry_{i}'] = inv_ntry
      self.invDict[f'entry_{i}'].bind("<KeyRelease>", lambda event, entry=inv_ntry: self.inv_search(alldicts, entry))

  def inv_search(self, list, entry):
    current_input = entry.get().lower()
    matching_names = [x for x in list if x.lower().startswith(current_input)]
    print(type(matching_names))
    print(matching_names)
    if len(matching_names) == 1:
      entry.delete(0, tk.END)
      entry.insert(0, matching_names[0])
