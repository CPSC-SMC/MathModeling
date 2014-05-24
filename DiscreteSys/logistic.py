# -*- coding: utf-8 -*-
"""
Epidemiology models

Created on Sun May 18 12:56:39 2014

@author: Steven
"""

from numpy import *
import matplotlib.pyplot as plt


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
    

def logistic_bif(size=100,iter=100,clear=False):
    """
    Plot points in the bifurcation diagram of the logistic map
    
    size --> the number of points to plot (default=100)
    """
    if clear:
        plt.close()
        plt.title("Logistic map bifurcation diagram")
        plt.xlabel(r"The logistic parameter $\lambda$")
        plt.ylabel(r"Approx. Periodic/Fixed point")
    for i in range(size):
        y = random.rand()
        a = random.rand()*4
        plot (a, logistic(y, a, iter),'.')

def logistic_cobweb(a=2, clear=False):
    """
    Plot a cobweb plot for the logistic map with parameter a. Clear the plot
    if clear = True
    """
    if clear:
        plt.close()
        plt.title(r"Logistic cobweb plot $\lambda=%f$" % (a))
        plt.xlabel(r"Previous step $y_{n-1}$")
        plt.ylabel(r"Current step $y_n$")

    # plot the curve y = x
    plot([0,1],[0,1],'b-')
    
    # plot the logistic map
    x = arange(0,1,0.01)
    plot(x,logistic(x,a),'g-')
    
    # choose an initial condition at random
    y = random.rand()
    plot([y,y],[0,y])
    
    # plot each segment of the cobweb plot
    for ynew in logistic_orbit(y, a):
        plot([y,y],[y,ynew])
        plot([y, ynew],[ynew,ynew])
        y = ynew

# fixed points of the logisic map
print logistic(0,1) # y = 0, a = 1
print 1./3, logistic(1./3,3./2) # y = 1/3, a = 3/2
print 1./2, logistic(1./2,2.) # y = 1/2, a = 2

# periodic points of the logistic map

# plot bifurcation diagram
logistic_bif(size=10000,clear=True)
