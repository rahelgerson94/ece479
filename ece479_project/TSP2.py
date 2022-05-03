#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:09:12 2022

@author: rahelmizrahi
"""


# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, startIdx):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != startIdx:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
     
    # permutations([1,2,3]) yields
    # (1, 2, 3)
    # (1, 3, 2)
    # (2, 1, 3)
    # (2, 3, 1) 
    # (3, 1, 2)
    # (3, 2, 1)
     
    
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = startIdx
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][startIdx]

        # update minimum
        min_path = min(min_path, current_pathweight)
        print(min_path)

    return min_path


# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
	graph = [[0, 10, 15, 20], 
             [10, 0, 35, 25],
			 [15, 35, 0, 30], 
             [20, 25, 30, 0]]
	print(travellingSalesmanProblem(graph, 0))

