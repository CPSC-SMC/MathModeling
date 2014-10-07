# -*- coding: utf-8 -*-
"""
Experimenting with data arrays

Created on Mon Oct  6 13:16:33 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

""" 
load the data
 Column 0: Wind Speed (m/s)
 Column 1: Wind Speed (MPH)
 Column 2: % at Wind Speed Class 4 Site
 Column 3: Annual Hours (h/yr)
 Column 4: Hours at Wind Speed (h/yr)
 Column 5: Power Curve Data (W)
 Column 6: Annual Energy Generation (kWh/yr)
"""

data = np.genfromtxt('windpower.txt',delimiter=',')

plt.figure(0)
plt.plot(data[:,1], data[:,5],'o')

plt.figure(1)
plt.plot(np.log(data[:,1]), np.log(data[:,5]), 'o')

A = np.array([[1]*len(data[1:,1]),np.log(data[1:,1])]).T
Y = np.array([np.log(data[1:,5])]).T

b = np.linalg.solve(np.dot(A.T,A), np.dot(A.T,Y))

def power_curve(x,b):
    return np.exp(b[0])*x**b[1]


x = np.linspace(0,54,21)

plt.figure(0)
plt.plot(x, power_curve(x, b))
print 'b =', b.T