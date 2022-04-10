#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 05:55:09 2022

@author: rahelmizrahi
"""

n = int(input("Enter the size of list : "))
print("\n")
numList  = []
for i in range(n):
    numList.append(list(map(int, input("Enter the list numbers separated by space ").strip().split()))[:n])
    print("User List: ", numList)