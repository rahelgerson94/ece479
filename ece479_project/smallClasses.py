#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:55:52 2022

@author: rahelmizrahi
"""

class waterStand:
    def __init__(self, Type):
        self.Type = Type #chilled or room temp

class Bottle:
    def __init__(self, capacity, material):
            self.capacity = lower(capacity) #4 gallons or 6 gallons
            self.material = lower(material) #plastic or glass

class waterColumn:
    def __init__(self):
            self.waterStand = None #4 gallons or 6 gallons
            self.bottle = None #plastic or glass
    
    def addWaterStand(self, waterStandObj):
        self.waterStand = waterStandObj
   
    
   def addBottle(self, bottleObj):
        self.bottle = bottleObj
        
        
if __name__ == "__main__":
