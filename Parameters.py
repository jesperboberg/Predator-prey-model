'''
Created on 20 Nov 2020

@author: jesperboberg
'''
import numpy as np

def parameters():
    para1 = 5
    para2 = 12
    para3 = 'x'
    return locals()

# Tmp Parameters based on Eq(20 and 22) in
# Extended Lotka–Volterra equations incorporating population heterogeneity: Derivation and analysis of the predator–prey case
# with tmp values
def environmentParameters():
    gridSize = 100
    Q = 2                       # Nr of patches
    alpha = np.array([[0, 0.002], [0.000125, 0]])  # Interraction
    rScaleForest = 1
    rScaleField = 0.6
    hScaleForest = 1
    hScaleField = 0.6
    return locals()


def preyParameters():
    r = 0.02           # Growth rate of popoulation
    a = 0.01           # Static component of linear model (by Iwao)
    b = 1           # Linear component of linear model (by Iwao)
    h = 0.02/500           # Intrinsic limitations on growth r/K (K carrying capacity)

    return locals()


def predatorParameters(): #Tmp values
    v = 0.05
    return locals()
