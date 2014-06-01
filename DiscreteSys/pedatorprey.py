# -*- coding: utf-8 -*-
"""
Discrete predator prey dynamics

Created on Mon May 19 14:00:12 2014

@author: sbroad
"""

import matplotlib.pyplot as plt

def predprey(x,y,a,b,c,d):
    dx = x*(a-b*y)
    dy = y*(d*x-c)
    #print dx, dy
    return (max(x+dx,0),max(y+dy,0))

# set up parameters and initial conditions
a = 0.01
b = 0.01
c = 0.10
d = 0.002
x = 100
y = 5

prey = []
pred = []
time = range(20)

# calculate the populations over time
for i in time:
    prey.append(x)
    pred.append(y)
    (x,y) = predprey(x,y,a,b,c,d)

# graph the populations versus time
plt.close(1)
plt.figure(1)
plt.title('Predator and prey populations over time')
plt.xlabel('Time periods')
plt.ylabel('Population')
plt.plot(time,prey,'r-',label='Prey population')
plt.plot(time,pred,'b--', label='Predator population')
plt.legend(loc='best')

# graph predators vs. prey
plt.close(2)
plt.figure(2)
plt.title('Predator vs. Prey Population')
plt.xlabel('Prey Population')
plt.ylabel('Predator Population')
plt.plot(prey,pred,'g-+')

