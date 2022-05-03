#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:38:42 2022

@author: rahelmizrahi
"""
import shelf as shelf
#from robot import Robot
#import robot as Robot
from smallClasses import WaterStand, Bottle, WaterColumn
/Users/rahelmizrahi/Downloads/ece479_project/AIPS.py
class AIPS:
    def __init__(self, distGrid):
        self.EmptyShelf = shelf.EmptyShelf() 
        self.FullShelf = shelf.FullShelf()
        self.WaterColumn = WaterColumn() 
        self.distanceGrid = distGrid
        
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
        
        
        ''' Robot Actions '''
        # technician leaves two full bottles on the ground
        newBottle1 = Bottle(4, "plastic")
        newBottle2 = Bottle(4, "plastic")
        oldBottle = Bottle(4, "plastic")
        
        # call on robot to restock
        done = robot.Robot().changeBottles(newBottle1, newBottle2, oldBottle)
        
        if done == True:
            print("bottles have been restocked")
            
        
    
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
    
    '''sound the alarm if a leak is detected '''
    def needAlarm(self):
        for b in self.FullShelf.Bottles:
            if b.leak == True:
                return True
       
    # implementation of traveling Salesman Problem
    def travellingSalesmanProblem( self, s, goal):
        V = len(self.distGrid[0]) 
        # store all vertex apart from source vertex
        vertex = []
        for i in range(V):
            if i != s:
                vertex.append(i)

        # store minimum weight Hamiltonian Cycle
        min_path = maxsize
        permList=permutations(vertex)

        # permutations([1,2,3]) yields
        # (1, 2, 3)
        # (1, 3, 2)
        # (2, 1, 3)
        # (2, 3, 1)
        # (3, 1, 2)
        # (3, 2, 1)
        paths = []
        for path in permList:
            path = self.truncateTuple(path, goal)
            if not( path in paths):
                # store current Path weight(cost)
                current_pathweight = 0
        
                # compute current path weight
                currSrc = s
                for currDst in path:
                    print("currSrc = {}, currDst = {}".format(currSrc, currDst))
                    current_pathweight += self.distGrid[currSrc][currDst]
                    path = currDst
                current_pathweight += self.distGrid[currSrc][s]
        
                # update minimum
                min_path = min(min_path, current_pathweight)
                print(min_path)
                paths.append(path)

        return min_path

    '''helper fct'''
    def truncateTuple( self, tupl, goal):
        tmp = []  
        for node in tupl:
            if node != goal:
                tmp.append(node)
            else:
                tmp.append(node)
                break
        return tuple(tmp)
        
        
