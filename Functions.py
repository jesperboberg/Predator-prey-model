"""
Created on 20 Nov 2020

@author: jesperboberg
"""
import numpy as np
import random
from Parameters import parameters


def createLattice(forestSize, preyPop, predatorPop):
    lattice = []
    for i in range(forestSize):
        empty_lists = [[] for _ in range(forestSize)]
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


def moveRandom(animal, animalList, lattice):
    paraList = parameters()
    forestSize = paraList['forestSize']
    r = random.randint(1, 4)
    x = animal[0]
    y = animal[1]

    speed = 1
    dx = random.randint(-speed, speed)
    dy = random.randint(-speed, speed)
    while (dx == 0 and dy == 0) or (dx != 0 and dy != 0):
        dx = random.randint(-speed, speed)
        dy = random.randint(-speed, speed)
    lattice[(x + dx) % forestSize][(y + dy) % forestSize].append(animal[2])
    lattice[x][y].remove(animal[2])
    animalList.remove(animal)
    animalList.append([(x + dx) % forestSize, (y + dy) % forestSize, animal[2]])
    return lattice, animalList
    '''

    if (r == 1):
        lattice[(x + 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x + 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if (r == 2):
        lattice[x][(y + 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y + 1) % forestSize, animal[2]])
        return lattice, animalList
    if (r == 3):
        lattice[(x - 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x - 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if (r == 4):
        lattice[x][(y - 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y - 1) % forestSize, animal[2]])
        return lattice, animalList
    return lattice, animalList
    '''


def moveSemiRandom(animal, animalList, lattice):
    paraList = parameters()
    forestSize = paraList['forestSize']
    r = random.randint(1, 4)
    x = animal[0]
    y = animal[1]
    if ('prey' in lattice[(x + 1) % forestSize][y]):
        lattice[(x + 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x + 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if ('prey' in lattice[x][(y + 1) % forestSize]):
        lattice[x][(y + 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y + 1) % forestSize, animal[2]])
        return lattice, animalList
    if ('prey' in lattice[(x - 1) % forestSize][y]):
        lattice[(x - 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x - 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if ('prey' in lattice[x][(y - 1) % forestSize]):
        lattice[x][(y - 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y - 1) % forestSize, animal[2]])
        return lattice, animalList
    if (r == 1):
        lattice[(x + 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x + 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if (r == 2):
        lattice[x][(y + 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y + 1) % forestSize, animal[2]])
        return lattice, animalList
    if (r == 3):
        lattice[(x - 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x - 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if (r == 4):
        lattice[x][(y - 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y - 1) % forestSize, animal[2]])
        return lattice, animalList
    return lattice, animalList


def movePredator(animal, animalList, lattice, densities):
    paraList = parameters()
    forestSize = paraList['forestSize']
    prob = np.array(densities)
    prob = prob + 1
    prob = prob / sum(prob)
    prob = np.cumsum(prob)
    r = random.random()
    x = animal[0]
    y = animal[1]
    if ('prey' in lattice[(x + 1) % forestSize][y]):
        lattice[(x + 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x + 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if ('prey' in lattice[x][(y + 1) % forestSize]):
        lattice[x][(y + 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y + 1) % forestSize, animal[2]])
        return lattice, animalList
    if ('prey' in lattice[(x - 1) % forestSize][y]):
        lattice[(x - 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x - 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if ('prey' in lattice[x][(y - 1) % forestSize]):
        lattice[x][(y - 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y - 1) % forestSize, animal[2]])
        return lattice, animalList
    if (r < prob[0]):
        lattice[(x)][(y + 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y + 1) % forestSize, animal[2]])
        return lattice, animalList
    if (r < prob[1]):
        lattice[(x + 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x + 1) % forestSize, y, animal[2]])
        return lattice, animalList
    if (r < prob[2]):
        lattice[x][(y - 1) % forestSize].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([x, (y - 1) % forestSize, animal[2]])
        return lattice, animalList
    if (r <= prob[3]):
        lattice[(x - 1) % forestSize][y].append(animal[2])
        lattice[x][y].remove(animal[2])
        animalList.remove(animal)
        animalList.append([(x - 1) % forestSize, y, animal[2]])
        return lattice, animalList
    # return lattice,animalList


def countPrey(x, y, lattice):
    count = 0
    sq = lattice[x][y]
    for animal in sq:
        if (animal == 'prey'):
            count = count + 1
    return count


def preyDensity(xStart, yStart, lattice, R, siz):
    north = 0
    for y in range(1, R):
        for x in range(-y, y):
            north = north + countPrey((xStart + x) % siz, (yStart + y) % siz, lattice)

    south = 0
    for y in range(1, R):
        for x in range(-y, y):
            south = south + countPrey((xStart + x) % siz, (yStart - y) % siz, lattice)

    east = 0
    for x in range(1, R):
        for y in range(-x, x):
            east = east + countPrey((xStart + x) % siz, (yStart + y) % siz, lattice)

    west = 0
    for x in range(1, R):
        for y in range(-x, x):
            west = west + countPrey((xStart - x) % siz, (yStart + y) % siz, lattice)
    return north, east, south, west


def updateLattice(lattice, preyList):
    for i, row in enumerate(lattice):
        for j, lis in enumerate(row):
            if len(lis) > 1 and 'predator' in lis:
                for animal in lis:
                    if animal == 'prey':
                        preyList.remove([i, j, animal])
                        lattice[i][j].remove(animal)

    return lattice, preyList


def addPredators(lattice, predList, change):
    while (True):
        if (change == 0):
            return lattice, predList
        if (change < 0):
            r = random.randint(0, len(predList) - 1)
            temp = predList.pop(r)
            lattice[temp[0]][temp[1]].remove('predator')
            change += 1
        if (change > 0):
            x = random.randint(0, len(lattice[0]) - 1)
            y = random.randint(0, len(lattice[0]) - 1)
            lattice[x][y].append('predator')
            predList.append([x, y, 'predator'])
            change -= 1


def addPrey(lattice, preyList, change):
    while (True):
        if (change == 0):
            return lattice, preyList
        if (change < 0):
            r = random.randint(0, len(preyList) - 1)
            temp = preyList.pop(r)
            lattice[temp[0]][temp[1]].remove('prey')
            change += 1
        if (change > 0):
            x = random.randint(0, len(lattice[0]) - 1)
            y = random.randint(0, len(lattice[0]) - 1)
            lattice[x][y].append('prey')
            preyList.append([x, y, 'prey'])
            change -= 1


def createRandomPrey(paraDict):
    preyPopulation = []
    amount = paraDict['preyPopulationSize']
    forestSize = paraDict['forestSize']
    for i in range(amount):
        x = random.randint(0, forestSize - 1)
        y = random.randint(0, forestSize - 1)
        assert x < forestSize
        assert y < forestSize
        preyPopulation.append([x, y, 'prey'])
    return preyPopulation


def createRandomPredator(paraDict):
    predatorPopulation = []
    amount = paraDict['predatorPopulationSize']
    forestSize = paraDict['forestSize']
    for i in range(amount):
        x = random.randint(0, forestSize - 1)
        y = random.randint(0, forestSize - 1)
        assert x < forestSize
        assert y < forestSize
        predatorPopulation.append([x, y, 'predator'])
    return predatorPopulation


def populationSizes(forest, outsideForest):
    predatorsForest = 0
    predatorsOutside = 0
    preyForest = 0
    preyOutside = 0
    return predatorsForest, predatorsOutside, preyForest, preyOutside


def prayGrowthPatchEst(nPray, nPredator, alpha12, prayParameters):
    rGrowth = prayParameters['r']
    hLimit = prayParameters['h']
    a = prayParameters['a']
    b = prayParameters['b']
    dN = rGrowth * nPray - nPray * hLimit(a + b * nPray + 1) - hLimit * alpha12 * nPredator * nPray
    return dN


def predatorGrowthPatchEst(nPray, nPredator, alpha21, predatorParameters):
    v = predatorParameters['v']

    dN = alpha21 * nPray * nPredator - v * nPredator
    return dN


def growthEst():
    dNPrayForest = prayGrowthPatchEst()

    dNPredator = 0
    dNPray = 0
    dN = [dNPray, dNPredator]
    return
