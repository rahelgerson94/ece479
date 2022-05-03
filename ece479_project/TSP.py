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
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s, goal):
    V = 5
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
        path = truncateTuple(path, goal)
        if not( path in paths):
            # store current Path weight(cost)
            current_pathweight = 0
    
            # compute current path weight
            currSrc = s
            for currDst in path:
                print("currSrc = {}, currDst = {}".format(currSrc, currDst))
                current_pathweight += graph[currSrc][currDst]
                path = currDst
            current_pathweight += graph[currSrc][s]
    
            # update minimum
            min_path = min(min_path, current_pathweight)
            print(min_path)
            paths.append(path)

    return min_path

'''truncates perms so that each tup in perms ends with goal node '''
def truncatePermuations( listOfTuples, goal): 
    goalPermutations = []
    for tup in tuples: 
        truncTuple = truncateTuple(tup, goal)
        if truncTuple not in goalPermutaions:
            goalPermutations.append(truncTuple)
    return truncTuples
        
def truncateTuple( tupl, goal):
    tmp = []  
    for node in tupl:
        if node != goal:
            tmp.append(node)
        else:
            tmp.append(node)
            break
    return tuple(tmp)
    
        
# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
    graph = [[0, 10, 15, 20], 
             [10, 0, 35, 25],
			 [15, 35, 0, 30], 
             [20, 25, 30, 0]]
    goal = 3
    start = 2
    print( "min cost from node{} to node{} is {}.".format(start, goal, travellingSalesmanProblem(graph, start, goal)))
    # perms = permutations([1,2,3])
    # for perm in perms:
    #     print(truncateTuple(perm, 2))
    
   