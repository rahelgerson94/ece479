#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:38:42 2022

@author: rahelmizrahi
"""
import shelf as shelf
from smallClasses import WaterStand, Bottle, WaterColumn

class AIPS:
    def __init__(self):
        self.EmptyShelf = shelf.EmptyShelf()
        self.FullShelf = shelf.FullShelf()
        self.WaterColumn = WaterColumn()
        
    def replenish(self):
        ''' issued if there is only 1 bottle left on the full-bottle shelf 
            and the water level in the bottle on the water stand drops below 1/4 gallon.
        '''
        assert self.FullShelf.getNumBottles() == 1, "we only replenish if number of bottles equals 1 and its cap. is less than 0.25 gal.\nNum bottles equals {}".format(self.FullShelf.getNumBottles())
        #2 wb's dropped off at the full bottle shelf.
        
        wbFull = Bottle(4, 'plastic')
        wbFull.setLevel(4)
        self.FullShelf.addWaterBottle(wbFull)
        self.FullShelf.addWaterBottle(wbFull)
        self.EmptyShelf.Bottles = [] #empty bottles collected by technician
        self.FullShelf.vstacked = True 
       
        print("num bottles : {}" .format(self.FullShelf.numBottles))
        print("empty bottles : {}" .format(self.EmptyShelf.numBottles))
        print("full shelf has been restacked")
    
    def needReplenish(self):
        f = False
        '''check is conditions for replenishing are met  '''
        if len(self.FullShelf.Bottles) == 1:
            if self.FullShelf.Bottles[0].currLevel <= 0.25:
                f = True
        return f
    
    def needReplace(self):
        if self.WaterColumn.Bottle.currLevel == 0:
            return True
        else:
            return False
    def replace(self):
        # robott puts empty bottle on the empty bottle shelf
        self.EmptyShelf.Bottles.insert(0, self.WaterColumn.Bottle)
        self.WaterColumn.Bottle = None 
        #pick a full bottle from the full bottle shelf, place it on the water bottle stand
        fullBottle = self.FullShelf.Bottles.pop()
        self.WaterColumn.Bottle = fullBottle
       
    
        