"""
simple classes for roulette sim experiments

RSlot: definition of a slot on the wheel. Slots have a name (looks like a number bt has
    both "0" and "00" and a color which may be red, black, or green).

RMatDiv: a roulette mat is divided into several areas including "number" bets and various
    combo bets like "Red" or "10-36" - each with a different payout rule - plus connections
    for various split bets (as part of their condion method(s))

    in American, when eitehr zero appears all bets but on the zero are lost. In French,
    bets are halved ("partage")

Bet: each bet has a "dollar" value and is assigned to a mat value. Includes split bets
      "en chaval" -- bet placed across two, three, or four boundaries, or on a column edge
      (six numbers)

Player: each player has a bankroll value, and can create one or more bets per overall system
     turn. Each player has a personal history of running bank values.

Game: a game consists of a wheel, a mat, one or more players, and a history of how players
     are doing relative to the house.
"""

import os
import sys
from enum import Enum

class Color(Enum):
  RED = 1
  BLACK = 2
  GREEN = 3

class RSlot:
  def __init__(self,Name,Color):
    self.name = Name
    self.color = Color

class RMatDiv:
  def __init__(self,Name,Payout=None,Condition=None):
    "Payout may be a lambda expression, or None to use the default"
    self.name = Name
    if Payout is not None:
      self.payout = Payout
    if Condition is not None:
      self.condition = Condition

def make_wheel(American=True):
  wheel = {}
  redlist = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
  for i in range(1,36):
    name = i.__str__()
    wheel[name] = RSlot(name, Color.RED if i in redlist else Color.BLACK)
  wheel["0"] = RSlot("0", Color.GREEN)
  if American:
    wheel["00"] = RSlot("00", Color.GREEN)
  return wheel

def make_mat(American=True):
  divs = {}
  for i in range(1,36):
    name = i.__str__()
    divs[i] = RMatDiv(name) # default for normal numeric values
  divs["0"] = RMatDiv("0") # TODO: lambda expression
  if American:
    divs["00"] = RMatDiv("00") # TODO: lambda expression
    divs["2to1A"] = RMatDiv("2to1") # TODO: lambda expression & condition (range(1,34,3))
    divs["2to1B"] = RMatDiv("2to1") # TODO: lambda expression & condition (range(2,35,3))
    divs["2to1C"] = RMatDiv("2to1") # TODO: lambda expression & condition (range(3,36,3))
    divs["1st12"] = RMatDiv("3to1") # TODO: lambda expression & condition (range(1,12)) #prem douzaine
    divs["2nd12"] = RMatDiv("3to1") # TODO: lambda expression & condition (range(13,24)) # moyennne d.
    divs["3rd12"] = RMatDiv("3to1") # TODO: lambda expression & condition (range(25,36)) #dernier d.
    divs["1-18"] = RMatDiv("1-18") # TODO: lambda expression & condition (range(1,18)) # manque
    divs["19-36"] = RMatDiv("19-36") # TODO: lambda expression & condition (range(19,36)) # passe
    divs["ODD"] = RMatDiv("ODD") # TODO: lambda expression & condition # Impair
    divs["EVEN"] = RMatDiv("EVEN") # TODO: lambda expression & condition # Pair
    divs["RED"] = RMatDiv("RED") # TODO: lambda expression & condition
    divs["BLACK"] = RMatDiv("BLACK") # TODO: lambda expression & condition


if __name__ == "__main__":
  w = make_wheel()
  print(w.keys())
  print("okay")