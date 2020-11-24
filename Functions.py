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

def prayGrowthPatchEst(nPray,nPredator,alpha12,prayParameters):
    rGrowth = prayParameters['r']
    hLimit = prayParameters['h']
    a = prayParameters['a']
    b = prayParameters['b']
    dN = rGrowth*nPray-nPray*hLimit(a+b*nPray+1)-hLimit*alpha12*nPredator*nPray
    return dN


def predatorGrowthPatchEst(nPray,nPredator,alpha21,predatorParameters):
    v = predatorParameters['v']

    dN = alpha21*nPray*nPredator - v*nPredator
    return dN

def growthEst():

    dNPrayForest = prayGrowthPatchEst()

    dNPredator = 0
    dNPray = 0
    dN = [dNPray, dNPredator]
    return