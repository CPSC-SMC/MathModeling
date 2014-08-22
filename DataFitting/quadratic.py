# -*- coding: utf-8 -*-
"""
Linear least squares

Created on Fri Aug 22 11:41:12 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

# the x and y data
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.12, 0.24, 0.72, 1.30, 1.90])

# plot this data
plt.plot(x, y, '+')

# fit the data
p = np.polyfit(x, y, 2) # the two is the degree of the polynomial
print p

# make a function from the polynomial fit
f = np.poly1d(p)

# plot the fit function
X = np.linspace(-1, 5, 21) # a range of values that encompass all x data
plt.plot(X, f(X),'--')

# plot the fits for the original data points
plt.plot(x, f(x), 'o')
