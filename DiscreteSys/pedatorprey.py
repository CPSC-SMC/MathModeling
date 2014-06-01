# -*- coding: utf-8 -*-
"""
Discrete predator prey dynamics

Created on Mon May 19 14:00:12 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def predprey(x,y,a,b,c,d,t=1):
    """
    This is an update function for the predator-prey model.
    x = prey population
    y = predator population
    delta x = (a*x - b*x*y)*t
    delta y = (-c*y + d*x*y)*t
    """
    for step in range(1/t):
        x += x * (a - b*y) * t
        y += y * (d*x - c) * t
    return (x,y)

# setup parameters
x = 100
y = 5
a = 1.1
b = 0.1
c = 1 
d = 0.01

# setup prey and pred lists
prey = []
pred = []
step = range(2000)
for i in step:
    prey.append(x)
    pred.append(y)
    (x,y) = predprey(x,y,a,b,c,d)

# Plot a time graph
plt.close(1)
plt.figure(1)
plt.title('Prey and Predator populations vs. time')
plt.xlabel('Time periods')
plt.ylabel('Populations')
plt.plot(step, prey, 'b-+', label='Prey')
plt.plot(step,pred,'r-o',label="Predator")
plt.legend(loc='best')

# Plot a phase graph
#plt.close(2)
plt.figure(2)
plt.title('Predator vs. Prey population')
plt.xlabel('Prey population')
plt.ylabel('Predator population')
plt.plot(prey,pred,'-o',label='V=%.2f' % (-d*x+c*np.log10(x)+b*y+a*np.log10(y)))
plt.legend(loc='best')
