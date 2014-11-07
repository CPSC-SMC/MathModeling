# -*- coding: utf-8 -*-
"""
Random walk (1D)

Created on Fri Nov  7 10:19:56 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

p = 0.5 # probability of moving right

def bernoulli(x, p = 0.5):
    """
    Shift +1 for right, -1 for left
    """
    return x + (1 if np.random.uniform() <= p else -1)

#pos = 0
# Four steps of a random walk
#pos = bernoulli(pos, p); print pos
#pos = bernoulli(pos, p); print pos
#pos = bernoulli(pos, p); print pos
#pos = bernoulli(pos, p); print pos

def rw(xinit = 0, p = 0.5, steps = 4):
    """
    Perform several steps of a random walk
    """
    x = xinit
    for i in range(steps):
        x = bernoulli(x, p)
    return x

xfin = np.array([rw(steps=9) for i in range(10000)])
plt.hist(xfin)

# simpler algorithm uses binomial random variable
def rw1d(xinit = 0, p = 0.5, steps = 4):
    """ perform several steps of a 1D random walk using binomial r.v. """
    right = np.random.binomial(steps, p)    
    #return xinit + right - (steps - right)
    return xinit + 2*right - steps

xfin = np.array([rw1d(steps=9) for i in range(10000)])
plt.hist(xfin)