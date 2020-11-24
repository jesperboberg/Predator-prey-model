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
    prob = growthProb(100,20,50,2)
    print(prob[0])
    print(prob[1])
    print(prob[2])
    print(prob[3])


main()
