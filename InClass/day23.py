# -*- coding: utf-8 -*-
"""
One variable logistic regression: test data

Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import math

def sigmoid(x1, b0, b1): 
    t = b0 + x1*b1
    return 1 / (1 + np.exp(-t))

def rescale(arr,lower=0.0,upper=1.0):
    v=arr.copy()
    return (v-min(v))/(max(v)-min(v)) * abs(upper-lower) + min([lower,upper])


# raw data
data = np.genfromtxt("xgradedata.csv",delimiter=',',dtype='float')
kap = np.array(filter(lambda x: not(math.isnan(x[2]) or math.isnan(x[8])),data))

# kaplan
passed = kap[:,2] # passed the nursing exam
kaplan = kap[:,8]/100

plt.plot(kaplan,passed,'o')

b, pscov = opt.curve_fit(sigmoid, kaplan, passed)  
print 'Cutoff is', -b[0]/b[1]*100,'on Kaplan'

xp = np.linspace(min(kaplan), max(kaplan), 51)

# Plot the results
plt.plot(xp, sigmoid(xp, b[0], b[1]), '-')
plt.xlabel('x')
plt.ylabel('y',rotation='horizontal') 
plt.ylim(ymin = -0.1, ymax=1.1)
plt.grid(True)
plt.show()

