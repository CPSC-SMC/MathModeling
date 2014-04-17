# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 20:36:45 2014

@author: Steven
"""

import numpy as np
import matplotlib.pyplot as plt

logo = np.uint64( plt.imread('logo.gif'))
logoR = dot(transpose(logo[:,:,1]),logo[:,:,1])
logoG = dot(transpose(logo[:,:,2]),logo[:,:,2])
logoB = dot(transpose(logo[:,:,3]),logo[:,:,3])
lTl[:,:,0] = logoR
lTl[:,:,1] = logoG
lTl[:,:,2] = logoB
plt.imshow(lTl)
