# -*- coding: utf-8 -*-
"""
Population model

Created on Tue May 20 14:13:18 2014

@author: Steven
"""
import numpy as np
import matplotlib.pyplot as plt

# Unconstrained growth
#   D y(n) = a * y(n)
#   y(n) = (1+a)**n * y(0)
unconstrained = lambda n, y0, a: (1+a)**n * y0


# calculate the growth rate
# y(n) = (1+a)**n * y(0)
# ln [y(n)/y(0)] = n*ln(1+a)
# a = (y(n)/y(0))**(1/n)-1
y0 = 100
y12 = 200
a = (2)**(1./12)-1
plt.plot(unconstrained(np.arange(0,20),y0,a)) 

# Constrained growth
# max_pop is the maximum population
# min_pop is the minimum population (probably zero)
# y0 is the initial population
# a is the parameter
# D y (n) = a * (y(n)-min_pop) * (max_pop-y(n)) / (M-m)**2
plt.close()
max_pop = 1000.
min_pop = 0.
y0 = 100.
a = .05
constrained_update = lambda y, a, M, m = 0: y + a*(y-m)*(M-y)

def constrained_gen(y0,a,M,m=0,size=100):
    y = y0
    for i in range(size):
        yield y
        y = constrained_update(y,a,M,m)

    yield y
        
i = 0
for y in constrained_gen(y0,a,max_pop,min_pop):
    i+=1
    plt.plot(i,y,'o')
    
