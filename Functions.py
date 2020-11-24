'''
Created on 20 Nov 2020

@author: jesperboberg
'''
import numpy as np
import random

from Basic_model.Parameters import parameters

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
        animalList.append([animal[0]+1,animal[1],animal[2]])
    if(r == 3 and animal[0] > 0):
        lattice[animal[0]-1][animal[1]].append(animal[2])
        lattice[animal[0]][animal[1]].remove(animal[2])
        animalList.remove(animal)
        animalList.append([animal[0]+1,animal[1],animal[2]])            
    if(r == 4 and animal[1] > 0):
        lattice[animal[0]][animal[1]-1].append(animal[2])
        lattice[animal[0]][animal[1]].remove(animal[2])
        animalList.remove(animal)
        animalList.append([animal[0]+1,animal[1],animal[2]])            
    return lattice,animalList    
        
def updateLattice(lattice,preyList):
    print('hmm')
    for row in lattice[:]:
        for lis in row:
            if(len(lis) > 1):
                for animal in lis:
                    if(animal[2] == 'predator'):
                        predatorInList = True
                for animal in lis:
                    if(animal[2] == 'prey' and predatorInList):
                        preyList.remove(animal)
                        lattice[animal[0]][animal[1]].remove(animal[2])
    return lattice,preyList

def createRandomPrey(paraDict):
    preyPopulation = []
    amount = paraDict['preyPopulationSize']
    forestSize = paraDict['forestSize']
    for i in range(amount):
        preyPopulation.append([random.randint(0,forestSize-1),random.randint(0,forestSize-1),'prey'])
    return preyPopulation

def createRandomPredator(paraDict):
    predatorPopulation = []
    amount = paraDict['predatorPopulationSize']
    forestSize = paraDict['forestSize']
    for i in range(amount):
        predatorPopulation.append([random.randint(0,forestSize-1),random.randint(0,forestSize-1),'predator'])
    return predatorPopulation

def populationSizes(forest,outsideForest):
    predatorsForest = 0
    predatorsOutside = 0
    preyForest = 0
    preyOutside = 0
    return predatorsForest,predatorsOutside,preyForest,preyOutside


    
