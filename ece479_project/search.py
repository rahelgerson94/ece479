#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:35:01 2022

@author: rahelmizrahi
"""

# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
import numpy as np
class search:
    def __init__(self, grid):
        self.grid = grid
        self.nodeMap = ['origin', 'A', 'B', 'C', 'D', 'E']
    # implementation of traveling Salesman Problem
    def TSP(self, s, goal):
        # store all vertex apart from source vertex
        V = len(self.grid[0])
        vertex = []
        for i in range(V):
            if i != s and i!= 0:
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
                    #print("currSrc = {}, currDst = {}".format(currSrc, currDst))
                    current_pathweight += self.grid[currSrc][currDst]
                    path = currDst
                current_pathweight += self.grid[currSrc][s]
        
                # update minimum
                min_path = min(min_path, current_pathweight)
                #print(min_path)
                paths.append(path)
    
        return min_path
    
    '''truncates perms so that each tup in perms ends with goal node '''
    def truncatePermuations( self, listOfTuples, goal): 
        goalPermutations = []
        for tup in tuples: 
            truncTuple = truncateTuple(tup, goal)
            if truncTuple not in goalPermutaions:
                goalPermutations.append(truncTuple)
        return truncTuples
            
    def truncateTuple( self, tupl, goal):
        tmp = []  
        for node in tupl:
            if node != goal:
                tmp.append(node)
            else:
                tmp.append(node)
                break
        return tuple(tmp)
        
    def visit(self, src, prevGoals):
        distances =  [self.TSP( src, dst) for dst in range(0,6)] 
        goal = 10000000
        for i, dst in enumerate(distances):
            if i  not in prevGoals:
                goal = min(goal, distances[i])
        node = np.where(np.array(distances) == goal)[0][0]
        print("[SEARCH] from {}, we will visit customer {} \n".format(self.nodeMap[src], self.nodeMap[node]))
        return goal, node
        
            
    
    
# Driver Code
if __name__ == "__main__":
    pass

    # # matrix representation of graph
    # graph = [[0, 10, 15, 20], 
    #          [10, 0, 35, 25],
    #          [15, 35, 0, 30], 
    #          [20, 25, 30, 0]]
    # goal = 3
    # start = 2
    # print( "min cost from node{} to node{} is {}.".format(start, goal, travellingSalesmanProblem(graph, start, goal)))
    # # perms = permutations([1,2,3])
    # # for perm in perms:
    # #     print(truncateTuple(perm, 2))
    
   