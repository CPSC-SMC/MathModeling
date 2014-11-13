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

def sigmoid(x, b0, b1, b2): 
    t = b0 + x[0]*b1 + x[1]*b2
    return 1 / (1 + np.exp(-t))

def rescale(arr,lower=0.0,upper=1.0):
    v=arr.copy()
    return (v-min(v))/(max(v)-min(v)) * abs(upper-lower) + min([lower,upper])

def is_complete(x):
    return not isnan(x[1]) and not isnan(x[3]) and not isnan(x[5])
    
# raw data
data = np.genfromtxt("xgradedata.csv",delimiter=',',dtype='float')
data = np.array(filter(is_complete, data))

x1 = data[:,3] # kaplan
x2 = data[:,5] # sci gpa
y = data[:,1] # license exam

passed = np.where(y==1)
nopass = np.where(y==0)

plt.plot(x1[passed],x2[passed],'x')
plt.plot(x1[nopass],x2[nopass],'o')
"""
plt.figure(0)
plt.plot(x1,y,'o')
plt.title('license exam results vs. kaplan pretest')

plt.figure(1)
plt.plot(x2,y,'o')
plt.title('license exam results vs. cumulative gpa')
"""

# divide kaplan by 100 and gpa by 4 
coeff, pscov = opt.curve_fit(sigmoid, np.array([x1/100,x2/4]), y)
m = -coeff[1]/coeff[2]
b = -coeff[0]/coeff[2]

print m, b

xs = np.linspace(50,52,2)
ys = ((m*xs/100)+b)*4

plt.plot(xs,ys,'-')

