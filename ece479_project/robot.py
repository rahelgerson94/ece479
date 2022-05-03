#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:54:35 2022

@author: rahelmizrahi & jazlandavis
"""

from smallClasses import Bottle as Bottle

class robot:
    
    ''' robot starts off with empty hand and holding nothing '''
    def __init__(self):
        self.holding = False
        self.handempty = True
        self.object = Bottle(4, "plastic")
        
    def c(self, new1, new2, old):
        ''' 1. pickup bottle(old) from shelf '''
        if self.handempty == True and old.clear == True and old.inshelf == True:
            self.holding = True
            self.object = old
            self.handempty = False
        
        ''' 2. putdown bottle(old) on the flooself '''
        if self.holding == True and self.object == old:
            old.clear = True
            old.inshelf = False
            old.onfloor = True
            self.handempty = True
            self.holding = False
        
        ''' 3. pickup bottle(new1) from floor '''
        if self.handempty == True and new1.clear == True and new1.onfloor == True:
            self.holding = True
            self.object = new1
            self.handempty = False
            new1.onfloor = False
        
        ''' 4. putdown bottle(new1) on the shelf '''
        if self.holding == True and self.object == new1:
            new1.onshelf = True
            new1.clear = True
            self.handempty = True 
            self.holding = False
            
        
        ''' 5. pickup bottle(new2) from the floor '''
        if new2.clear == True and new2.onfloor == True and self.handempty == True:
            self.holding = True
            self.object = new2
            self.handempty = False
            new2.onfloor = False
            
        
        ''' 6. stack bottle(new2) on top of bottle(new1) in the shelf '''
        if self.holding == True and self.object == new2 and new1.clear == True:
            new2.clear = True
            self.handempty = True
            new1.clear = False
            new1.top = new2
        
        ''' 7. pickup bottle(old) from the floor '''
        if old.clear == True and old.onfloor == True and self.handempty == True:
            self.holding = True
            self.object = old
            self.handempty = False
            old.onfloor = False
        
        ''' 8. stack bottle(old) on top of bottle(new2) in the shelf'''
        if self.holding == True and self.object == old and new2.clear == True:
            old.clear = True
            self.handempty = True
            new2.clear = False
            new2.top = old
            
        if old.clear == True and new2.top == old and new1.top == new2:
            return True
        else:
            return False
        

if __name__ == "__main__":
    pass
