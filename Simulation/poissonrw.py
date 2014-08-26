# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 10:03:05 2014

@author: sbroad
"""
import numpy as np
import numpy.random as rdm
import matplotlib.pyplot as plt

# 2D poisson random walk 
# (exponentially distributed distance, uniformly distributed)

# expected migration distance
mu = 1

# create two arrays of x,y coordinate data (filled with zeros)
# these arrays store the trajectories of an individual random walk (e.g., shark)
x = np.zeros(100)
y = np.zeros_like(x)

# create two arrays for statistical data 
# we are going to track the movements of many random walks and record the 
# maximum distance from the origin, total distance traveled and trajectory
# diameter (greatest distance between two points)
max_dist = np.zeros(100)
tot_dist = np.zeros_like(max_dist)
diameter = np.zeros_like(max_dist)
final_x = np.zeros_like(max_dist)
final_y= np.zeros_like(max_dist)

# prepare a trajectory plot
plt.close()
plt.subplot(221)
plt.title('"Shark" trajectories')
plt.axis('off')

# There are several "sharks" to track... each iteration through the outer
# loop is one "shark"
for j in range(len(max_dist)):
    
    # draw random numbers, far->distance traveled, direction->angle [0,2pi)
    distances = rdm.exponential(scale=mu, size=len(x)-1)
    angles = rdm.uniform(high=2*np.pi,size=len(x)-1)
    
    # Each "shark" makes several "migrations", some long, some short
    for (d,theta,i) in zip(distances, angles,range(len(angles))):
        
        # adjust the "shark's" location
        x[i+1] = x[i] + d*np.cos(theta)
        y[i+1] = y[i] + d*np.sin(theta)
        
        # store the current maximum distance from origin
        max_dist[j] = max(max_dist[j],np.sqrt(x[i+1]**2 + y[i+1]**2))
        
        # store the current total distance
        tot_dist[j] += d
        
        # calculate and store the revised diameter
        dist = max([np.sqrt(a**2 + b**2) for a, b in zip(x-x[i+1],y-y[i+1])])
        diameter[j] = max(dist, diameter[j])
        
    # store the final position
    final_x[j] = x[-1]
    final_y[j] = y[-1]
    
    # plot the trajectory
    plt.plot(x, y, '-o')

# show statistics about the trajectories
plt.subplot(222)
plt.title('Trajectory statistics')
plt.hist(max_dist,label='Max. Dist. from Origin')

# show statistics about the trajectories
plt.subplot(222)
plt.hist(tot_dist,label='Tot. Dist. Traveled')

# show statistics about the trajectories
plt.subplot(222)
plt.hist(diameter,label='Trajectory Diameter')
plt.legend()

# show statistics about the trajectories
plt.subplot(223)
plt.title('Final Position histogram')
plt.hist2d(final_x, final_y)

plt.subplot(224)
plt.title('Final Position scatterplot')
plt.plot(final_x, final_y, 'o')