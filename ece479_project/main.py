#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:21:53 2022

@author: rahelmizrahi
"""

from smallClasses import WaterStand, Bottle, WaterColumn
from shelf import FullShelf, EmptyShelf
from AIPS import AIPS
import numpy as np
from search import search
#import robot as Robot 



'''create the grid representing distance between customers'''
#          0  A  B   C   D   E
grid  = [[0, 1, 1, 14, 15, 16], # 0
         [1, 0, 10, 15, 20, 30], # A
         [1, 10, 0, 35, 25, 14, ], # B
         [14, 15, 35, 0, 30, 17], # C
         [15, 20, 25, 30, 0, 9],  # D
         [16, 30, 14, 17, 9, 0]]  # E


''' WATER BOTTLES '''
wb1 = Bottle(4, 'plastic')
wb_full = Bottle(4, 'plastic')
wb_full.setLevel(4)

'''the AIPS obj has columns and shelves that are empty'''
a1 = AIPS(grid, 'TEST')
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


''' create 5 custumers '''
customers = [
    AIPS(grid, 'disptach') ,
    AIPS(grid, 'A'), #0
    AIPS(grid, 'B'), #1
    AIPS(grid, 'C'), #2
    AIPS(grid, 'D'), #3
    AIPS(grid, 'E'),#4
    ]




'''create  a  search object to find optimal dispatch routes '''
search = search(grid)
''' all customers are need of relenishing! need to do TSP to figure out shortest path'''
''' let's assume were currently at the dispatch center, which has index 0'''
visited = []
src = 0 #dispatch
nextDst = search.visit( src, visited )
''' replenish A '''
customers[nextDst].replenish()
'''add A to visted set '''
visited.append(nextDst)

''' now we need to visit the next custumer! let's find out who this will be '''
src = nextDst
nextDst = search.visit( src, visited )
visited.append(nextDst)






