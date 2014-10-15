# -*- coding: utf-8 -*-
"""
Two variable logistic regression

Created on Tue Oct 14 23:13:03 2014

@author: Steven
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
from math import isnan

def sigmoid(x1, b0, b1): 
    t = b0 + x1*b1
    return 1 / (1 + np.exp(-t))

def rescale(arr,lower=0.0,upper=1.0):
    v=arr.copy()
    return (v-min(v))/(max(v)-min(v)) * abs(upper-lower) + min([lower,upper])

def complete_data(x):
    return not (isnan(x[2]) or isnan(x[8]) or isnan(x[23]))
    
# raw data
data = np.genfromtxt("xgradedata.csv",delimiter=',',dtype='float')
data = np.array(filter(complete_data, data))[:,[2,8,23]]

p = np.where(data[:,0]==1)[0]
f = np.where(data[:,0]==0)[0]

plt.plot(data[p,1]/100,data[p,2],'bo')
plt.plot(data[f,1]/100,data[f,2],'ro')

b, pscov = opt.curve_fit(sigmoid, data[:,1]/100, data[:,0])  
print b
print 'Cutoff is', -b[0]/b[1],'on Kaplan'

xp = np.linspace(min(data[:,1]/100), max(data[:,1]/100), 51)

# Plot the results
plt.plot(xp, sigmoid(xp, b[0], b[1]), '-')
plt.xlabel('x')
plt.ylabel('y',rotation='horizontal') 
#plt.ylim(ymin = -0.1, ymax=1.1)
plt.grid(True)
plt.show()
