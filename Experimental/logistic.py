# -*- coding: utf-8 -*-
"""


Created on Wed Oct  8 14:30:46 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def logistic(x, b):
        
    
data = np.genfromtxt('KidCreative.csv',delimiter=',')

x = data[1:,2] # income
y = data[1:,1] # purchase


plt.plot(x, y, '.')
plt.ylim(ymin = -0.1, ymax = 1.1)
