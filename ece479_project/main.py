#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:21:53 2022

@author: rahelmizrahi
"""

from smallClasses import WaterStand, Bottle, WaterColumn
from shelf import FullShelf, EmptyShelf
from AIPS import AIPS

import robot as Robot 


    

wb1 = Bottle(4, 'plastic')
wb_full = Bottle(4, 'plastic')
wb_full.setLevel(4)

'''the AIPS obj has columns and shelves that are empty'''
a1 = AIPS()
a1.FullShelf.addWaterBottle(wb_full) #add a wb to TOP of shelf
a1.FullShelf.addWaterBottle(wb1) 

x = a1.needReplenish() #returns FALSE bc we have two bottles.  of top bottle == 0
a1.FullShelf.printBottles()

a1.FullShelf.removeWaterBottle(1) #remove the full bottle so that now we have 1 bottle w/ 0 gallons
x = a1.needReplenish() #returns true 

a1.FullShelf.printBottles()

a1.FullShelf.Bottles[0].setLevel(1) #set the wb level to 1 gallon 
x = a1.needReplenish() #returns False bc currLevel is 1, which is gt than 1/4

a1.FullShelf.printBottles()

a1.FullShelf.Bottles[0].setLevel(0) #set the wb level to 0 gallon 
x = a1.needReplenish() #returns False bc currLevel is 1, which is gt than 1/4

if x == True:
    a1.replenish()
    
''' replace if bottle on the water stand is empty'''
replace = a1.needReplace()
if replace == True: 
    a1.replace()