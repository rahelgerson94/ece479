#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:18:45 2022

@author: rahelmizrahi
"""
from pprint import pprint
import numpy as np
class Node:
    def __init__(self,data,level,fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data, -1)
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.move(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children
        
    def move(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            

    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):
        """ Specifically used to find the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []
        self.goal = [[1, 2, 3], [8, -1, 4], [7, 6, 5]]
    def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,start):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return self.h(start.data)+start.level

    def h(self,start):
        """ Calculates the difference between the given puzzles """
        temp = 0
        for i, row in enumerate(start):
            for j, cell in enumerate(row):
                if cell != self.goal[i][j]  and start[i][j] != -1:
                    #print(str(cell), str(self.goal[i][j])) 
                    temp += 1
        return temp
        

    def process(self):
        """ Accept Start and Goal Puzzle state"""
        print("Enter the start state matrix \n")
        #initStateData = self.accept()
        initStateData = [[2, 8, 3], [1, 6, 4], [7, -1, 5]]
        #print("Enter the goal state matrix \n")        
        

        initStateNode = Node(initStateData,0,0)
        initStateNode.fval = self.f(initStateNode)
        print(initStateNode.fval)
        """ Put the start node in the open list"""
        self.open.append(initStateNode)
        print("\n\n")
        for i in range(200):
            cur = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for row in cur.data:
                print(*row)
                #print("i = {}".format(i))
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(cur.data) == 0):
                print(i)
                break
            ''' otherwise, expand the state space (move U,D,L,R) '''
            for node_child in cur.generate_child():
                node_child.fval = self.f(node_child) #caluclate the f() value for each of the moves generated
                self.open.append(node_child)
            self.closed.append(cur)
            ''' now that  we've explored all this node's children, remove it from the open list'''
            del self.open[0]

            """ sort the opne list based on f value """
            self.open.sort(key = lambda x:x.fval,reverse=False)
if __name__ == "__main__":

    puz = Puzzle(3)
    puz.process()