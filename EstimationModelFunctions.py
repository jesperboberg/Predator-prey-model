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
    alpha = environmentalParam['alpha']
    if environmentType == 0:
        rGrowth = preyParam['r'] * environmentalParam['rScaleField']
        hLimit = preyParam['h'] * environmentalParam['hScaleField']
        alpha01 = alpha[0,1]*environmentalParam['alphaScaleField']
    elif environmentType == 1:
        rGrowth = preyParam['r'] * environmentalParam['rScaleForest']
        hLimit = preyParam['h'] * environmentalParam['hScaleForest']
        alpha01 = alpha[0,1]*environmentalParam['alphaScaleForest']
    else:
        rGrowth = 0
        hLimit = 0
        alpha01=0



    dN = rGrowth*nPrey-nPrey*hLimit*(a+b*nPrey+1)-hLimit*alpha01*nPredator*nPrey
    return dN


def predatorGrowthPatchEst(nPrey,nPredator,predatorParameters,environmentalParam,environmentType):
    v = predatorParameters['v']
    alpha = environmentalParam['alpha']
    if environmentType == 0:
        alpha10 = alpha[1,0]*environmentalParam['alphaScaleField']
    elif environmentType == 1:
        alpha10 = alpha[1,0]*environmentalParam['alphaScaleForest']
    else:
        alpha10=0

    dN = (alpha10*nPrey - v)*nPredator
    return dN

def growthEst(nPreyForest,nPredatorForest,nPreyField,nPredatorField):
    environmentalParam = Parameters.environmentParameters()
    preyParam = Parameters.preyParameters()
    predatorParam = Parameters.predatorParameters()

    forest = 1
    dNPreyForest = preyGrowthPatchEst(nPreyForest,nPredatorForest,preyParam,environmentalParam,forest)
    dNPredatorForest = predatorGrowthPatchEst(nPreyForest,nPredatorForest,predatorParam,environmentalParam,forest)

    field = 0
    dNPreyField = preyGrowthPatchEst(nPreyField,nPredatorField,preyParam,environmentalParam,field)
    dNPredatorField = predatorGrowthPatchEst(nPreyField,nPredatorField,predatorParam, environmentalParam,field)

    dN = [dNPreyForest, dNPredatorForest, dNPreyField, dNPredatorField]
    return dN

def growthProb(nPreyForest,nPredatorForest,nPreyField,nPredatorField):

    dN = growthEst(nPreyForest,nPredatorForest,nPreyField,nPredatorField)
    dNPreyForest = dN[0]
    dNPredatorForest = dN[1]
    dNPreyField = dN[2]
    dNPredatorField = dN[3]

    if nPreyForest < 1:
        probPreyForest = 0
    else:
        probPreyForest = dNPreyForest/nPreyForest
    if nPredatorForest < 1:
        probPredForest = 0
    else:
        probPredForest = dNPredatorForest/nPredatorForest
    if nPreyField < 1:
        probPreyField = 0
    else:
        probPreyField = dNPreyField/nPreyField
    if nPredatorField < 1:
        probPredField = 0
    else:
        probPredField = dNPredatorField/nPredatorField
    prob = [probPreyForest, probPredForest, probPreyField, probPredField]
    return prob