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
from TSP import TSP
#import robot as Robot 

nodeMap = ['origin', 'A', 'B', 'C', 'D', 'E']

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
dispatch = AIPS(grid, 'origin') 
A = AIPS(grid, 'A') #0
B = AIPS(grid, 'B') #1
C = AIPS(grid, 'C') #2
D = AIPS(grid, 'D') #3
E = AIPS(grid, 'E') #4


''' all customers are need of relenishing! need to do TSP to figure out shortest path'''
''' let's assume were currently at the dispatch center, which has index 0'''
distances =  [TSP(grid, 0, dst) for dst in range(0,6)]   #distances from origin to every node 
nodeToVist0 = np.argmin(distances)
print("from origin, we will visit customer {}  ".format(  nodeMap[nodeToVist0]))
A.replenish()

''' now we need to visit the next custumer! let's find out who this will be '''
distances =  [TSP(grid, nodeToVist0, dst) for dst in range(0,6)] 
nodeToVist1 = np.argmin(distances)
print("from {}, we will visit customer {}  ".format(nodeMap[nodeToVist0], nodeMap[nodeToVist1]))



