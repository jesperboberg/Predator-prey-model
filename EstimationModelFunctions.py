'''
Created on 24 Nov 2020

@author: sambern
'''
import numpy as np
import Parameters
import random


def preyGrowthPatchEst(nPrey,nPredator,preyParam,environmentalParam,environmentType):
    a = preyParam['a']
    b = preyParam['b']
    if environmentType == 0:
        rGrowth = preyParam['r'] * environmentalParam['rScaleField']
        hLimit = preyParam['h'] * environmentalParam['hScaleField']
    elif environmentType == 1:
        rGrowth = preyParam['r'] * environmentalParam['rScaleForest']
        hLimit = preyParam['h'] * environmentalParam['hScaleForest']
    else:
        rGrowth = 0
        hLimit = 0

    alpha = environmentalParam['alpha']
    dN = rGrowth*nPrey-nPrey*hLimit*(a+b*nPrey+1)-hLimit*alpha[0, 1]*nPredator*nPrey
    return dN


def predatorGrowthPatchEst(nPrey,nPredator,predatorParameters,environmentalParam):
    v = predatorParameters['v']
    alpha = environmentalParam['alpha']

    dN = (alpha[1, 0]*nPrey - v)*nPredator
    return dN

def growthEst(nPreyForest,nPredatorForest,nPreyField,nPredatorField):
    environmentalParam = Parameters.environmentParameters()
    preyParam = Parameters.preyParameters()
    predatorParam = Parameters.predatorParameters()

    forest = 1
    dNPreyForest = preyGrowthPatchEst(nPreyForest,nPredatorForest,preyParam,environmentalParam,forest)
    dNPredatorForest = predatorGrowthPatchEst(nPreyForest,nPredatorForest,predatorParam,environmentalParam)

    field = 0
    dNPreyField = preyGrowthPatchEst(nPreyField,nPredatorField,preyParam,environmentalParam,field)
    dNPredatorField = predatorGrowthPatchEst(nPreyField,nPredatorField,predatorParam, environmentalParam)

    dN = [dNPreyForest, dNPredatorForest, dNPreyField, dNPredatorField]
    return dN

def growthProb(nPreyForest,nPredatorForest,nPreyField,nPredatorField):

    dN = growthEst(nPreyForest,nPredatorForest,nPreyField,nPredatorField)
    dNPreyForest = dN[0]
    dNPredatorForest = dN[1]
    dNPreyField = dN[2]
    dNPredatorField = dN[3]

    probPreyForest = dNPreyForest/nPreyForest
    probPredForest = dNPredatorForest/nPredatorForest
    probPreyField = dNPreyField/nPreyField
    probPredField = dNPredatorField/nPredatorField

    prob = [probPreyForest, probPredForest, probPreyField, probPredField]
    return prob