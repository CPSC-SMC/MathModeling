# -*- coding: utf-8 -*-
"""
Logistic Map

Created on Sun May 18 12:56:39 2014

@author: Steven
"""

from numpy import *

# define an updating function
def logistic(y, a, n = 1):
    for i in range(n):
        y = a*y*(1-y)
    
    return y

def logistic_orbit(y0, a, size=100, period=1):
    vals = [y0]
    for i in range(size):
        vals += [logistic(vals[-1], a, period)]
    
    return vals
    

y = random.rand() # initial value of y is in range [0,1)
a = 1.5 # a is the parameter and should be between 0 and 4

for i in range(100):
    y = random.rand()
    print (y, logistic_orbit(y, 3.2, 2)[-1])

# fixed points of the logisic map
print logistic(0,1) # y = 0, a = 1
print 1./3, logistic(1./3,3./2) # y = 1/3, a = 3/2
print 1./2, logistic(1./2,2.) # y = 1/2, a = 2

# periodic points of the logistic map
