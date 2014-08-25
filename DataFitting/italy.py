# -*- coding: utf-8 -*-
"""
General curve fitting

Created on Fri Aug 22 12:10:17 2014

@author: sbroad
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Limited (constrained) growth (Italy)
# p. 109 - 114 Population Models

# the model function
def italy(t, M, B, k):
    return M/(1+B*np.exp(-M*k*(t-1915))) # formula from p. 109

# the data p. 102 (populations in millions)
year = np.array([1915, 1921, 1928, 1931, 1936, 1940, 1943, 1946, 1948])
pop = np.array([35.240, 37.270, 41.168, 42.119, 42.528, 45.330, 45.801, 45.646, 45.706])

# plot the data
plt.close()
plt.plot(year, pop, '+')

# curve fit the data using the italy (logistic) model
# italy is the model function
# p0 is an initial guess for the parameters M, B, k
popt, pcov = curve_fit(italy, year, pop, p0=[46,1,0.00001]) 
print popt

M = popt[0]
B = popt[1]
k = popt[2]

# plot the fit curve
Year = np.linspace(1910,1970,61)
plt.plot(Year, italy(Year, M, B, k), '--')

# plot the fit values for each data point
plt.plot(year, italy(year, M, B, k), 'o')

# Use the model to predict the population of Italy in 2014
print 'Predicting the population of Italy in 2014:', italy(2014,M,B,k), 'million'

