# -*- coding: utf-8 -*-
"""
Experimenting with multicolumn NumPy arrays

Created on Mon Oct  6 10:22:58 2014

@author: sbroad
"""

# -*- coding: utf-8 -*-
"""
Experimenting with a NumPy array

Created on Mon Oct  6 11:06:13 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def crit(x): # x represents our data
    """
    The criterion for filtering our data.
    x ---> our input data, row-by-row
    returns ---> true if the criterion is satisfied
                 false otherwise
    """
    return 10 <= x[0] <= 14

# load the data
data = np.genfromtxt('driving.txt', delimiter=',')
# filter the data
data = np.array(filter(crit,data))
# plot the filtered data
plt.plot(data[:,0], data[:,2])

# how many data points?
n = len(data[:,0])
print 'n =',n

# Ab = Y
A = np.array([ [1]*n, data[:,0] ]).T
Y = np.array([data[:,2]]).T

# solve A^T A b = A^T Y
b = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, Y))

# plot the estimated regression equation
t = np.linspace(10,14,21)
plt.plot(t, b[0] + b[1]*t)
