'''
Created on 20 Nov 2020

@author: jesperboberg
'''
from Parameters import parameters
from Predator import Predator
from Prey import Prey
from Functions import createRandomForest


def main():
    paraDict = parameters()
    p1 = paraDict['para1']
    print(paraDict['para3'])
    print(p1)



main()
