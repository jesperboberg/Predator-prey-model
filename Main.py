'''
Created on 20 Nov 2020

@author: jesperboberg
'''
from Parameters import parameters
from Predator import Predator
from Prey import Prey
from Functions import createRandomForest
from EstimationModelFunctions import growthProb
from EstimationModelFunctions import growthEst
import matplotlib
import matplotlib.pyplot as plt


def main():
    current = 0
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

#        print("It: " + str(current))
#        print(preyForest)
#        print(predatorForest)
#        print(preyField)
#        print(predatorField)
main()
