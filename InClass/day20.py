# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 09:31:20 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('limited-growth.txt',delimiter=',')

#print data

print data[1:4,0]

plt.plot(data[1:,1], data[1:,3], '+')