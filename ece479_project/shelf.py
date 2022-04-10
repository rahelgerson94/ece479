#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:49:51 2022

@author: rahelmizrahi
"""
class Shelf:
    def __init__(self):
        self.capacity = None

class vertShelf(Shelf):
    def __init__(self):
        self.capacity = 3 #bottles
class emptyShelf(Shelf):
    def __init__(self):
        self.capacity = 2 #bottles


if __name__ == "__main__":
