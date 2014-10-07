# -*- coding: utf-8 -*-
"""
Movie gross revenue

Created on Tue Oct  7 08:41:30 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import polyfit, polyval

data = np.genfromtxt('2013movies101-200.txt',delimiter=',')

plt.figure(0)
plt.plot(data[:,0], data[:,3],'o')

plt.figure(1)
plt.plot(np.log10(data[:,0]), np.log10(data[:,3]),'o')
b = polyfit(np.log10(data[:,0]),np.log10(data[:,3]),1)
print b
plt.plot(np.log10(data[:,0]),polyval(b,np.log10(data[:,0])))

plt.figure(2)
plt.plot(data[:,0], np.log10(data[:,3]),'o')
b = polyfit(data[:,0],np.log10(data[:,3]),1)
print b
plt.plot(data[:,0],polyval(b,data[:,0]))

plt.figure(3)
plt.plot(np.log10(data[:,0]), data[:,3],'o')

