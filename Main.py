'''
Created on 20 Nov 2020

@author: jesperboberg
'''

from Parameters import parameters
from EstimationModelFunctions import growthProb,growthEst,modelForest,modelField
import matplotlib
import matplotlib.pyplot as plt
from Functions import createLattice,moveRandom,createRandomPrey,createRandomPredator,updateLattice,addPredators,addPrey
import numpy as np 

def mainModel():
    #Deterministic model
    current = 0
    # Starting populations
    preyForest = [1000]
    predatorForest = [100]
    preyField = [1000]
    predatorField = [100]
    while current < 5000:
        prob = growthProb(preyForest[current],predatorForest[current],preyField[current],predatorField[current])
        preyForest.append((1+prob[0])*preyForest[current])
        predatorForest.append((1+prob[1])*predatorForest[current])
        preyField.append((1+prob[2])*preyField[current])
        predatorField.append((1+prob[3])*predatorField[current])
        current += 1
    x = [i for i in range(current+1)]

    plt.plot(x, preyForest,'b',x,predatorForest,'r',x,preyField,'g',x,predatorField,'orange')
    plt.show()
            
def mainSim():
    paraDict = parameters()
    preyPopulationForest = createRandomPrey(paraDict)
    predatorPopulationForest = createRandomPredator(paraDict)
    forest = createLattice(paraDict['forestSize'],preyPopulationForest,predatorPopulationForest)
    preyPop = [paraDict['preyPopulationSize']]
    predPop = [paraDict['predatorPopulationSize']]    
   
    # Plot setup
    '''plt.ion()
    fig, ax = plt.subplots()
    x = [prey[0] for prey in preyPopulationForest]
    y = [prey[1] for prey in preyPopulationForest]
    sc1 = ax.scatter(x,y,color = 'blue', s = 1)
    x = [predator[0] for predator in predatorPopulationForest]
    y = [predator[1] for predator in predatorPopulationForest]
    sc2 = ax.scatter(x,y,color = 'red', s = 1)
    plt.xlim(0,paraDict['forestSize'])
    plt.ylim(0,paraDict['forestSize'])
    plt.title('Forest with predators and prey')
    plt.draw()'''

    # Make a random movement for every prey/predator and update plots live
    for t in range(1,paraDict['timeSteps']):
        # Change the amount of prey and predators according to the model
        if(np.mod(t,paraDict['timeStepModel']) == 0):
            prob = modelForest(len(preyPopulationForest), len(predatorPopulationForest))
            changeInPredatorPop = prob[1]*len(predatorPopulationForest)
            changeInPredatorPop = int(np.round(changeInPredatorPop,0))
            changeInPreyPop = prob[0]*len(preyPopulationForest)
            changeInPreyPop = int(np.round(changeInPreyPop,0))
            forest, predatorPopulationForest = addPredators(forest,predatorPopulationForest,changeInPredatorPop)
            forest, preyPopulationForest = addPrey(forest,preyPopulationForest,changeInPreyPop)
        #print('Predators: ' + str(len(predatorPopulationForest)) + ' Prey: ' + str(len(preyPopulationForest)))
        for pred in predatorPopulationForest[:]:
            assert pred[2] in forest[pred[0]][pred[1]]
            forest, predatorPopulationForest = moveRandom(pred, predatorPopulationForest, forest)
        for prey in preyPopulationForest:
            assert prey[2] in forest[prey[0]][prey[1]]
            forest, preyPopulationForest = moveRandom(prey, preyPopulationForest, forest)

        forest,preyPopulationForest = updateLattice(forest, preyPopulationForest)
        #x = [prey[0] for prey in preyPopulationForest]
        #y = [prey[1] for prey in preyPopulationForest]
        #sc1.set_offsets(np.c_[x,y])
        #x = [predator[0] for predator in predatorPopulationForest]
        #y = [predator[1] for predator in predatorPopulationForest]
        #sc2.set_offsets(np.c_[x,y])
        #fig.canvas.draw_idle()
        #plt.pause(0.5)
        preyPop.append(len(preyPopulationForest))
        predPop.append(len(predatorPopulationForest))
    t = [t for t in range(0,len(preyPop))]
    plt.plot(t,preyPop,color = 'blue',label = 'Prey population size')
    plt.plot(t,predPop,color = 'red',label = 'Predator population size')
    plt.title('Model used every tenth time step')
    plt.legend()
    plt.show()
    print(preyPop[-1])
    print(predPop[-1])
    
mainSim()

