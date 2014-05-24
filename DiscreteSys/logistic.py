# -*- coding: utf-8 -*-
"""
Epidemiology models

Created on Sun May 18 12:56:39 2014

@author: Steven
"""

from numpy import *
from matplotlib.pyplot import *


# define the logistic map as an updating function
def logistic(y, a, n = 1):
    """
    The logistic map, y = a * y * (1-y).
    a --> the parameter, a value related to the communicability rate
    y --> the population proportion, the proportion (i.e., y in [0,1]) of infected
    n --> defaults to 1, the number of logistic iterations
    """
    for i in range(n):
        y = a*y*(1-y)
    
    return y

# a generator function for points in the logistic orbit of a certain initial condition
def logistic_orbit(y0, a, size=100, period=1):
    """
    Compute the forward partial orbit of the logistic map.
    
    y0     ---> the initial value in [0,1]
    a      ---> the parameter
    size   ---> the number of terms in the orbit
    period ---> the number of iterations per step (default = 1)
    """
    yield y0
    y = y0
    for i in range(size):
        y = logistic(y, a, period)
        yield y
    

# plot 100 random points in the bifurcation diagram of the logistic map
for i in range(100):
    y = random.rand()
    a = random.rand()*4
    plot (a, logistic(y, a, 1000),'.')

# plot a cobweb plot for the logistic map with a = 3.2
plot([0,1],[0,1],'b-')
x = arange(0,1,0.01)
plot(x,logistic(x,3.2),'g-')
y = random.rand()
plot([y,y],[0,y])
for ynew in logistic_orbit(y, 3.2):
    plot([y,y],[y,ynew])
    plot([y, ynew],[ynew,ynew])
    y = ynew

# fixed points of the logisic map
print logistic(0,1) # y = 0, a = 1
print 1./3, logistic(1./3,3./2) # y = 1/3, a = 3/2
print 1./2, logistic(1./2,2.) # y = 1/2, a = 2

# periodic points of the logistic map
