import tkinter as tk
from apifunctions import *

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
