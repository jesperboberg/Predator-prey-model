'''
Created on 20 Nov 2020

@author: jesperboberg
'''

def parameters():
    para1 = 5
    para2 = 12
    para3 = 'x'
    return locals()

# Tmp Parameters based on Eq(20 and 22) in
# Extended Lotka–Volterra equations incorporating population heterogeneity: Derivation and analysis of the predator–prey case
def environmentParameters():
    Q = 4                       # Nr of patches
    alpha = [[0,0.1],[-0.1,0]]  # Interraction
    return locals()


def preyParameters(): #Tmp values
    r = 0.001           # Growth rate of popoulation
    a = 0.002           # Static component of linear model (by Iwao)
    b = 0.003           # Linear component of linear model (by Iwao)
    h = 0.004           # Intrinsic limitations on growth

    return locals()


def predatorParameters(): #Tmp values
    v = 0.001
    return locals()
