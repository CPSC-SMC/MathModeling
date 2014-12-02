# -*- coding: utf-8 -*-
"""
Optimization: Functions of two variables

Created on Thu Nov 20 09:29:13 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = lambda x: x[0]**2 + (2-x[1]**2)**2 + x[1] + 2

fig = plt.figure(0)
ax = fig.gca(projection='3d')

xs, ys = np.meshgrid(np.linspace(-2,2,51), np.linspace(-2,2,51))
ax.plot_surface(xs,ys,f((xs,ys)),rstride=2, cstride=2,linewidth=0.1,edgecolor='w')

import scipy.optimize as opt

print opt.minimize(f, (0,2))

