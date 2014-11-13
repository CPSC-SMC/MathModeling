# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def sigmoid(x1,x2,b0,b1,b2):
    y = 1 / (1 + np.exp(-(b0+b1*x1+b2*x2)))
    return y

def rescale(arr,lower=0.0,upper=1.0):
    v=arr.copy()
    return (v-min(v))/(max(v)-min(v)) * abs(upper-lower) + min([lower,upper])

# raw data
data = np.genfromtxt("KidCreative.csv",delimiter=',',dtype='float')

x1 = data[1:,4] # married
x2 = data[1:,5] # college
y = data[1:,1] # purchase

xs = np.vstack([x1,x2])

print xs

#x=resize(x)
#y=resize(y)
ps, pcov = opt.curve_fit(sigmoid,xs,y)
print ps
xp = np.linspace(0, 1.1, 1500)
pxp=sigmoid(xp, ps[0], ps[1])

# Plot the results
plt.plot(xs, y, '.', xp, pxp, '-')
plt.xlabel('x')
plt.ylabel('y',rotation='horizontal') 
plt.grid(True)
plt.show()
