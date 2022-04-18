#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:49:51 2022

@author: rahelmizrahi
"""
class Shelf:
    def __init__(self):
        self.capacity = None
        
        self.Bottles = []
        self.numBottles = len(self.Bottles)
    
    def addWaterBottle(self, waterBottleObj):
        if self.getNumBottles() < self.capacity:
            self.Bottles.insert(0,waterBottleObj)
    
    def printBottles(self):
        for b in self.Bottles:
            print( "{}  " .format(b.currLevel) , delimter = ' ')
    def removeWaterBottle(self, idx):
        if self.numBottles < self.capacity:
            del self.Bottles[idx]
        self.printBottles()
            
    def getWaterBottle(self, index):
       assert index <= capacity - 1, " the index you requested must not exceed shelf's capacity, which is 3"
       return self.Bottles[index]
    def getNumBottles(self):
        return len(self.Bottles)
   
class FullShelf(Shelf):
    def __init__(self):
        self.capacity = 3 #bottles
        self.numBottles = 0
        self.Bottles = []
         

class EmptyShelf(Shelf):
    def __init__(self):
        self.capacity = 2 #bottles
        self.numBottles = 0
        self.Bottles = []


if __name__ == "__main__":
    f = FullShelf()