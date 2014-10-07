# -*- coding: utf-8 -*-
"""
Filtering a NumPy array

Created on Mon Oct  6 11:06:13 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('driving.txt', delimiter=',')

# y-acceration vs. time
plt.figure(0)
plt.plot(data[:,0], data[:,2])

def crit(x): # x represents our data
    return 10 <= x[0] <= 14 # going to return true or false
    # for each row

fltr = filter(crit, data)
data = np.array(fltr)

print data[0:3,:]

plt.figure(1)
plt.plot(data[:,0], data[:,2])
