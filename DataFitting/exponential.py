# -*- coding: utf-8 -*-
"""
Exponential least squares

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

# compute the log of all y values
logy = np.log(y)

# linear fit the logy data to the x data
p = np.polyfit(x, logy, 1) # the one is the degree of the polynomial
print p

# make a function from the polynomial fit
logf = np.poly1d(p)

# plot the fit function
X = np.linspace(-1, 5, 21) # a range of values that encompass all x data
# the fit is logarithmic so we must compose the exponential function
plt.plot(X, np.exp(logf(X)),'--')

# plot the fits for the original data points
plt.plot(x, np.exp(logf(x)), 'o')
