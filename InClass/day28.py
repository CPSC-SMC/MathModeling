# -*- coding: utf-8 -*-
"""
Interest rates

Created on Mon Nov 03 09:33:06 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

years = 50
runs = 100
inv = np.array([1000]*runs,dtype=float) # initial investment

for i in range(np.size(inv)):
    
    # random rates (parameter)
    rates = np.random.normal(loc=3.0,scale=1.0,size=years)
    
    for r in rates:
        inv[i] = inv[i]*(1+r/100)
    
print 'Expected value is $', np.mean(inv)
print 'Minimum value is $', np.min(inv)
print 'Maximum value is $', np.max(inv)

plt.hist(inv,bins=runs/10)

