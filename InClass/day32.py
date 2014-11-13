# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 09:08:31 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt


"""
One dimensional random walk
"""
n = 16 # number of steps per random walker
p = 0.5 # prob of moving right
k = 1000000 # number of walkers
w0 = 0

x = np.random.binomial(n,p,size=k)

w = w0 + 2*x - n

plt.figure(0)
plt.hist(w,bins=np.linspace(-n,n,n+1))

"""
Two dimensional random walk
"""

n = 15
p = [0.25, 0.50, 0.75, 1.00] # cumulative prob. of right, up, left, down
k = 10000
x = [0]*k
y = [0]*k

for j in range(n):
    # one step
    u = np.random.uniform(size=k)
    for i in range(np.size(u)):
        if u[i] <= 0.25:
            x[i] += 1
        elif u[i] <= 0.50:
            y[i] += 1
        elif u[i] <= 0.75:
            x[i] -= 1
        else:
            y[i] -= 1

plt.figure(1)
plt.hist2d(x,y,bins=range(-n,n+1,2))

