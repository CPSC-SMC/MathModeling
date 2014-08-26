# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 10:03:05 2014

@author: sbroad
"""

# 2D poisson random walk 
# (exponentially distributed distance, uniformly distributed)
x = np.zeros(100)
y = np.zeros(100)
far = rdm.exponential(size=100)
direction = rdm.uniform(high=2*np.pi,size=100)
for i in range(len(x)-1):
    x[i+1] = x[i] + far[i]*np.cos(direction[i])
    y[i+1] = y[i] + far[i]*np.sin(direction[i])

plt.figure(2)
plt.plot(x, y, '-o')
