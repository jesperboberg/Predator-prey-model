'''
Created on 20 Nov 2020

@author: jesperboberg
'''
import numpy as np
import random
from Parameters import parameters


def createLattice(forestSize,preyPop,predatorPop):
    lattice = []
    for i in range(forestSize):
        empty_lists = [ [] for _ in range(forestSize) ]
        lattice.append(empty_lists)
    for prey in preyPop:
        i = prey[0]
        j = prey[1]
        lattice[i][j].append('prey')
    for predator in predatorPop:
        i = predator[0]
        j = predator[1]
        lattice[i][j].append('predator')
    for prey in preyPop:
        assert lattice[prey[0]][prey[1]]
    for predator in predatorPop:
        assert lattice[predator[0]][predator[1]]
    return lattice


def moveRandom(animal,animalList,lattice): # Need to change in this to create field, this just works for closed forest
    paraList = parameters()
    forestSize = paraList['forestSize']
    r = random.randint(1,4)
    if(r == 1 and animal[0] < forestSize-1):
        lattice[animal[0]+1][animal[1]].append(animal[2])
        lattice[animal[0]][animal[1]].remove(animal[2]) # bugs at one of these, element that we are trying to remove doesnt exist in lattice....
        animalList.remove(animal)
        animalList.append([animal[0]+1,animal[1],animal[2]])
    if(r == 2 and animal[1] < forestSize-1):
        lattice[animal[0]][animal[1]+1].append(animal[2])
        lattice[animal[0]][animal[1]].remove(animal[2])
        animalList.remove(animal)
        animalList.append([animal[0],animal[1]+1,animal[2]])
    if(r == 3 and animal[0] > 0):
        lattice[animal[0]-1][animal[1]].append(animal[2])
        lattice[animal[0]][animal[1]].remove(animal[2])
        animalList.remove(animal)
        animalList.append([animal[0]-1,animal[1],animal[2]])
    if(r == 4 and animal[1] > 0):
        lattice[animal[0]][animal[1]-1].append(animal[2])
        lattice[animal[0]][animal[1]].remove(animal[2])
        animalList.remove(animal)
        animalList.append([animal[0],animal[1]-1,animal[2]])
    return lattice,animalList    


def updateLattice(lattice,preyList):
    for i, row in enumerate(lattice):
        for j, lis in enumerate(row):
            if len(lis) > 1 and 'predator' in lis:
                for animal in lis:
                    if animal == 'prey':
                        preyList.remove([i,j,animal])
                        lattice[i][j].remove(animal)

    return lattice,preyList

def addPredators(lattice,predList,change):
    while(True):
        if(change == 0):
            return lattice,predList
        if(change < 0):
            r = random.randint(0,len(predList)-1)
            temp = predList.pop(r)
            lattice[temp[0]][temp[1]].remove('predator')
            change += 1
        if(change > 0):
            x = random.randint(0,len(lattice[0])-1)
            y = random.randint(0,len(lattice[0])-1)
            lattice[x][y].append('predator')
            predList.append([x,y,'predator'])
            change -= 1 

def addPrey(lattice,preyList,change):
    while(True):
        if(change == 0):
            return lattice,preyList
        if(change < 0):
            r = random.randint(0,len(preyList)-1)
            temp = preyList.pop(r)
            lattice[temp[0]][temp[1]].remove('prey')
            change += 1
            print('Possible error, prey change negative')
        if(change > 0):
            x = random.randint(0,len(lattice[0])-1)
            y = random.randint(0,len(lattice[0])-1)
            lattice[x][y].append('prey')
            preyList.append([x,y,'prey'])
            change -= 1  
                       
def createRandomPrey(paraDict):
    preyPopulation = []
    amount = paraDict['preyPopulationSize']
    forestSize = paraDict['forestSize']
    for i in range(amount):
        x = random.randint(0,forestSize-1)
        y = random.randint(0,forestSize-1)
        assert x < forestSize
        assert y < forestSize
        preyPopulation.append([x,y,'prey'])
    return preyPopulation

def createRandomPredator(paraDict):
    predatorPopulation = []
    amount = paraDict['predatorPopulationSize']
    forestSize = paraDict['forestSize']
    for i in range(amount):
        x = random.randint(0,forestSize-1)
        y = random.randint(0,forestSize-1)
        assert x < forestSize
        assert y < forestSize
        predatorPopulation.append([x,y,'predator'])
    return predatorPopulation

def populationSizes(forest,outsideForest):
    predatorsForest = 0
    predatorsOutside = 0
    preyForest = 0
    preyOutside = 0
    return predatorsForest,predatorsOutside,preyForest,preyOutside

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