# -*- coding: utf-8 -*-
"""
Computing empirical cdfs

Created on Fri Oct 17 08:36:52 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def empirical_cdf(x,data=np.random.random(20)):
    sorted_data = np.sort(data,axis=None)    
    
            
xs = np.linspace(0,1, num=1000)
ys = empirical_cdf(xs)

print ys

plt.plot(xs,empirical_cdf(xs),'-')

data = np.genfromtxt('nelson3.12.txt',delimiter=',')


