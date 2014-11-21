# -*- coding: utf-8 -*-
"""
Day 35: The Copier Problem

Created on Wed Nov 19 08:57:39 2014

@author: sbroad
"""

import numpy as np

T = 0 # open the copier
S = [0, 0] # the initial state
n = 0 # step number

mu_G = 6.0 # the average time between customers
mu_X = 4.6 # average order completion time

C = [0, np.inf, np.inf, np.inf]

while not np.isinf(np.min(C)):
    
    T = np.min(C) # what time it
    I = np.argmin(C) # which event was triggered
    
    if I == 0: # open the copier
        C[0] = np.inf # don't need to open the store again
        C[1] = np.random.exponential(scale=mu_G)
        C[3] = 270
        
    # customer arrives
    elif I == 1:
        
        # if the copier is available, just use it
        if S[1] == 0:
            S[1] = 1
            C[2] = T + np.random.exponential(scale=mu_X)
            
        # if the copier is not available, stand in line
        else:
            S[0] += 1
            
        # find out when the next customer arrives
        C[1] = T + np.random.exponential(scale=mu_G)
        
    # customer finishes
    elif I == 2:
        
        # if there is no one left in line
        if S[0] == 0:
            S[1] = 0 # now the copier is available
            C[2] = np.inf # no one is making copies
            
        # if there are more people in line
        else:
            S[0] -= 1 # one person from the line steps up to copy
            C[2] = T + np.random.exponential(scale=mu_X)

    # copier closes    
    elif I == 3:
        C[1] = np.inf # no more customers arriving
        C[3] = np.inf # we've already closed the copier
        #S[0] = 0 # all customers in line go home        
    
    else:    
        print "How did we get here? Event: ", I
        
    print n, I, T, S, C
        
