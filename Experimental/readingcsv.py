# -*- coding: utf-8 -*-
"""
Loading .csv text data in Python

Created on Mon Oct  6 08:32:47 2014

@author: sbroad
"""

# import numpy, pyplot
import numpy as np
import matplotlib.pyplot as plt


# open and read the file
data = np.genfromtxt('jumps.csv',delimiter=',')


# work with the array
# plot column 1 vs. column 0
plt.figure(0)
plt.plot(data[:,0], data[:,1])
print data[1,:]

# plot column 2 vs. column 1
plt.figure(1)
plt.plot(data[:,1], data[:,2])


# plot column 1 * column 2 vs. column 3 + column 4
plt.figure(2)
plt.plot(data[:,3] + data[:,4], data[:,1] * data[:,2])


