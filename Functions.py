'''
Created on 20 Nov 2020

@author: jesperboberg
'''
import numpy as np
import random


def createRandomForest(size,density):
    forest = np.zeros(shape = (size,size)) 
    amountTrees = np.floor(size*size*density)
    amountTrees = int(amountTrees)
    count = 0
    while count < amountTrees:
        randX = random.randint(0,size-1)
        randY = random.randint(0,size-1)
        if(forest[randX,randY] == 0):
            forest[randX,randY] = 1
            count += 1
    return forest
