#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:55:52 2022

@author: rahelmizrahi
"""

class WaterStand:
    def __init__(self, Type):
        self.Type = Type #chilled or room temp

class Bottle:
    def __init__(self, capacity, material ):
            self.capacity = capacity #4 gallons or 6 gallons
            self.criticalLevel = 0.25
            self.material = material.lower() #plastic or glass
            self.currLevel = 0
    def isLevelTooLow(self):
        if self.currLevel != None and self.currLevel <= self.criticalLevel:
            return True
    def setLevel(self, amt):
        #assert amt <= self.capacity, "error, amount cannot exceed capacity, which is {}" .format(self.capacity)
        self.currLevel = amt
class WaterColumn:
    def __init__(self):
            self.WaterStand = WaterStand("chilled") #4 gallons or 6 gallons
            self.Bottle = Bottle(4 , "plastic") #plastic or glass
    
    
    
    
        
        
if __name__ == "__main__":
    pass