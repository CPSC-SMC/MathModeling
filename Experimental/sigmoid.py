# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def sigmoid(x, b0, b1): 
    t = b0 + x*b1
    return 1 / (1 + np.exp(-t))

def rescale(arr,lower=0.0,upper=1.0):
    v=arr.copy()
    return (v-min(v))/(max(v)-min(v)) * abs(upper-lower) + min([lower,upper])

# raw data
data = np.genfromtxt("KidCreative.csv",delimiter=',',dtype='float')

x = data[1:,2]
xs = rescale(data[1:,2]) # income
y = data[1:,1] # purchase

#x=resize(x)
#y=resize(y)
bs, pscov = opt.curve_fit(sigmoid, xs, y)  
print bs

xp = np.linspace(min(xs), max(xs), 51)

# Plot the results
plt.plot(xs, y, '.')
plt.plot(xp, sigmoid(xp, bs[0], bs[1]), '-')
plt.xlabel('x')
plt.ylabel('y',rotation='horizontal') 
plt.grid(True)
plt.show()
