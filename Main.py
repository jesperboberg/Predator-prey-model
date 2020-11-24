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


def main():
    paraDict = parameters()
    p1 = paraDict['para1']
    print(paraDict['para3'])
    print(p1)
    current = 1
    preyForest = 100
    predatorForest = 20
    preyField = 100
    predatorField = 20
    while current < 500:
        prob = growthProb(preyForest,predatorForest,preyField,predatorField)
        preyForest += prob[0]*preyForest
        predatorForest += prob[1]*predatorForest
        preyField += prob[2]*preyField
        predatorField += prob[3]*predatorField
        print("It: " + str(current))
        print(preyForest)
        print(predatorForest)
        print(preyField)
        print(predatorField)
        current += 1


main()
