# -*- coding: utf-8 -*-
"""
Random Walk 2D

Created on Fri Nov  7 11:27:07 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def move(c,p=[0.25,0.25,0.25,0.25]):
    """
    Move one step on a rectangular grid.
    
    c ---> an array [x,y] where x is the previous x position
           and y is the previous y position
    p ---> an array with four elements that sum to at most 1
           p[0] ---> the probability of moving right
           p[1] ---> the prob of moving up
           p[2] ---> the prob of moving left
           p[3] ---> the prob of moving down
           1 - sum(p) ---> the prob of not moving
    """
    v = np.random.uniform()
    
    if v <= p[0]:
        return c + [1,0] # move right
    elif v <= sum(p[0:2]):
        return c + [0,1] # move up
    elif v <= sum(p[0:3]):
        return c + [-1,0]
    elif v <= sum(p):
        return c + [0,-1]
    
    # else do not move
    return c

plt.figure(0)
final = []
for j in range(1000):
    pos = [np.array([0,0])]
    
    for i in range(100):
        pos.append(move(pos[i]))
    
    pos = np.array(pos)
    plt.plot(pos[:,0],pos[:,1])
    final.append([pos[-1,0],pos[-1,1]])

final = np.array(final)
final_x = final[:,0]
final_y = final[:,1]

x_min = min(final_x)
x_max = max(final_x)
y_min = min(final_y)
y_max = max(final_y)
bin_sq = 2
shift = 0.5
#x_bins = np.linspace(x_min-shift,x_max+1-shift,np.ceil((x_max-x_min)/bin_sq))
#y_bins = np.linspace(x_min-shift,x_max+1-shift,np.ceil((x_max-x_min)/bin_sq))

plt.hist2d(final_x, final_y, bins=15, cmap=plt.cm.YlOrRd_r)
#plt.hist2d(final_x, final_y, bins=[x_bins, y_bins])
#plt.hexbin(final_x,final_y,gridsize=15, cmap=plt.cm.YlOrRd_r)
plt.xticks([])
plt.yticks([])