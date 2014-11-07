# -*- coding: utf-8 -*-
"""
Drive Thru Simulation

Created on Fri Nov  7 12:42:42 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

mu = 1.3 # customers arrive approximately every mu minutes
order = 1.0 # customers take 1 minute to order on average
order_sd = 0.2 # standard deviation of order time
max_wait = 5.0 # maximum time a customer is willing to wait
max_wait_sd = 1.0 # standard deviation of max wait time
n = 1000

arrivals = np.random.exponential(scale=mu,size=n)
orders = np.random.normal(loc = order, scale = order_sd, size=n)
max_waits = np.random.normal(loc = max_wait, scale = max_wait_sd, size=n)
arrived = 0
ordered = 0
left = []
arrival_times = []
ordered_times = []
wait_times = []
for (a, o, w) in zip(arrivals,orders,max_waits):
    arrived += a
    prev_ordered = ordered
    ordered = max(ordered,arrived) + max(o,0)
    wait = ordered - arrived
    if wait <= w:
        arrival_times.append(arrived)
        ordered_times.append(ordered)
        wait_times.append(wait)
    else:
        ordered = prev_ordered
        left.append([wait, w])

print len(left)*100/float(n), 
print 'percent of customers left without ordering'
wait_times = np.array(wait_times)

plt.figure(0)
plt.hist(wait_times)
plt.title('Wait times for customers who ordered')

left = np.array(left)

plt.figure(1)
plt.hist(left[:,0])
plt.title('Projected wait time of customers who left without ordering')

plt.figure(2)
plt.hist(left[:,0]-left[:,1])
plt.title('Amount of extra wait time customers are unwilling to wait')
