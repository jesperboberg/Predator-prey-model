'''
Created on 20 Nov 2020

@author: jesperboberg
'''

from Parameters import parameters
#from Predator import Predator
from Prey import Prey
from EstimationModelFunctions import growthProb
from EstimationModelFunctions import growthEst
import matplotlib
import matplotlib.pyplot as plt
from Functions import createLattice,moveRandom,createRandomPrey,createRandomPredator,updateLattice
import numpy as np 

def main():
    #Deterministic model
    current = 0
    preyForest = [1000]
    predatorForest = [100]
    preyField = [1000]
    predatorField = [100]
    while current < 200:
        prob = growthProb(preyForest[current],predatorForest[current],preyField[current],predatorField[current])
        preyForest.append((1+prob[0])*preyForest[current])
        predatorForest.append((1+prob[1])*predatorForest[current])
        preyField.append((1+prob[2])*preyField[current])
        predatorField.append((1+prob[3])*predatorField[current])
        current += 1
    x = [i for i in range(current+1)]

    plt.plot(x, preyForest,'b',x,predatorForest,'r',x,preyField,'g',x,predatorField,'orange')
    plt.show()


    paraDict = parameters()
    # Plot setup and initializing random populations
    plt.ion()
    fig, ax = plt.subplots()
    preyPopulationForest = createRandomPrey(paraDict)
    x = [prey[0] for prey in preyPopulationForest]
    y = [prey[1] for prey in preyPopulationForest]
    sc1 = ax.scatter(x,y,color = 'blue', s = 1)
    predatorPopulationForest = createRandomPredator(paraDict)
    x = [predator[0] for predator in predatorPopulationForest]
    y = [predator[1] for predator in predatorPopulationForest]
    sc2 = ax.scatter(x,y,color = 'red', s = 1)
    forest = createLattice(paraDict['forestSize'],preyPopulationForest,predatorPopulationForest)
    plt.xlim(0,paraDict['forestSize'])
    plt.ylim(0,paraDict['forestSize'])
    plt.title('Forest with predators and prey')
    plt.draw()
    # Make a random movement for every prey/predator and update plots live
    for t in range(paraDict['timeSteps']):
        print(t)
        for pred in predatorPopulationForest[:]:
            assert pred[2] in forest[pred[0]][pred[1]]
            forest, predatorPopulationForest = moveRandom(pred, predatorPopulationForest, forest)
        for prey in preyPopulationForest:
            assert prey[2] in forest[prey[0]][prey[1]]
            forest, preyPopulationForest = moveRandom(prey, preyPopulationForest, forest)

        forest,preyPopulationForest = updateLattice(forest, preyPopulationForest)
        x = [prey[0] for prey in preyPopulationForest]
        y = [prey[1] for prey in preyPopulationForest]
        sc1.set_offsets(np.c_[x,y])
        x = [predator[0] for predator in predatorPopulationForest]
        y = [predator[1] for predator in predatorPopulationForest]
        sc2.set_offsets(np.c_[x,y])
        fig.canvas.draw_idle()
        plt.pause(0.2)


main()
