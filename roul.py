"""
simple classes for roulette sim experiments

RSlot: definition of a slot on the wheel. Slots have a name (looks like a number bt has
    both "0" and "00" and a color which may be red, black, or green).
    Slots also have payout rules

RMatDiv: a roulette mat is divided into several areas including "number" bets and various
    combo bets like "Red" or "10-36"

Bet: each bet has a "dollar" value and is assigned to a mat value

Player: each player has a bankrool value, and can create one or more bets per overall system turn.
     Each player has a personal history of running bank values

Game: a game consists of a wheel, a mat, one or more players, and a history of how players
     are doing relative to the house.
"""

import os
import sys

class RSlot:
  def __init__(self,Name=None):
    if Name is not None:
      self.name = Name
    self.red = False

