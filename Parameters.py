'''
Created on 20 Nov 2020

@author: jesperboberg
'''
import numpy as np

def parameters():
    forestSize = 1000 
    preyPopulationSize = 1000
    predatorPopulationSize = 100
    timeSteps = 5000
    timeStepModel = 10
    visionRange = 30
    return locals()
def predatorParameters(): #Tmp values
    v = 0.05
    speed = 10
    pounceRange = 2 # 10 = forest base case, 2 = field case
    return locals()
# Tmp Parameters based on Eq(20 and 22) in
# Extended Lotka–Volterra equations incorporating population heterogeneity: Derivation and analysis of the predator–prey case
# with tmp values
def environmentParameters():
    gridSize = 100
    Q = 2                       # Nr of patches
    preyParam = preyParameters()
    predParam = predatorParameters()
    r = preyParam['r']
    K = preyParam['K']
    v = predParam['v']
    alpha = np.array([[0, 1/r], [v/(K*0.1), 0]])  # Interraction
    alphaScaleForest = 1
    alphaScaleField = 1.1
    rScaleForest = 1
    rScaleField = 0.6
    hScaleForest = 1
    hScaleField = 0.6
    return locals()


def preyParameters():
    r = 0.02            # Growth rate of popoulation
    K = 5000             # Carrying capacity
    a = 0             # Static component of linear model (by Iwao)
    b = 1               # Linear component of linear model (by Iwao)
    h = r/K             # Intrinsic limitations on growth r/K (K carrying capacity)

    speed = 10
    return locals()


