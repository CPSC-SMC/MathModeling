# -*- coding: utf-8 -*-
"""
Random walks

Created on Mon Aug 25 12:16:59 2014

@author: sbroad
"""
import numpy as np
import numpy.random as rdm
from matplotlib.pyplot import hist, hist2d
import matplotlib.pyplot as plt

# 1D random walk (binomial model)
def onedim(s, p=0.5, steps=1):
    for i in range(steps):
        draws = np.where(rdm.uniform(size=len(s))<p,1,-1)
        s += draws
    return s

plt.close(1)
plt.figure(1)
plt.subplot(321)
hist(onedim(np.zeros(10000),steps=1000),bins=30)
plt.title('Unbiased 1D random walk')

plt.subplot(322)
hist(onedim(np.zeros(10000),p=0.55,steps=1000),bins=30)
plt.title('Biased 1D random walk (p=0.55)')


# 2D random walk (NS/EW independent, nearest neighbor)
def twodim(x, y, pnorth=0.5, peast=0.5, steps=1):
    return onedim(x,p=peast,steps=steps),onedim(y,p=pnorth,steps=steps)

plt.subplot(323)
x, y = twodim(np.zeros(10000), np.zeros(10000), steps=1000)
hist2d(x, y,bins=20)
plt.title('Unbiased 2D nn random walk')


plt.subplot(324)
x, y = twodim(np.zeros(10000), np.zeros(10000), pnorth=0.55, steps=1000)
hist2d(x, y,bins=20)
plt.title('Northward bias 2D nn random walk')


plt.subplot(325)
x, y = twodim(np.zeros(10000), np.zeros(10000), peast=0.45, steps=1000)
hist2d(x, y,bins=20)
plt.title('Westward bias 2D nn random walk')








# 