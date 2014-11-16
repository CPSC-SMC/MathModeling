# -*- coding: utf-8 -*-
"""

Nelson: Exercise 2.7

Created on Thu Nov 13 11:17:48 2014

@author: sbroad

"""

import numpy as np
import matplotlib.pyplot as plt


"""
Calculate demand on any given day according to the data in the book.
"""
inv_f = np.array([415,704,214,856,620,353,172,976,735,433,217,860,598,833])
ordered = np.array([0 if (i%2==1 or q > 1000) else 1000- q for (i,q) in zip(range(np.size(inv_f)),inv_f)])
inv_i = np.concatenate(([700],(inv_f+ordered)[:-1]))

demd = inv_i-inv_f

mu = np.mean(demd)
sigma = np.std(demd)


"""
Implement the stochastic process

S(n) = (I(n),O(n),L(n),R(n))
I(n) = start of day inventory
O(n) = number ordered, orders only take place on odd days
                     , and received on even days
L(n) = number of lost sales
R(n) = number of completed sales

T(n) = day number, advances by 1 each day

Y(t) = state at time t

e0 = start simulation
e1 = customer buying hamburgers on a day
e2 = placing an order
e3 = receiving an order

"""

inv_init = 700
order_thresh = 500
inv_max = 1000

demand_mu = 250
demand_sigma = 50

C = [0, np.inf, np.inf, np.inf]
S = [700, 0, 0, 0]
N = 100
T = 0

out_f = open('state.csv', mode = 'w')
out_f.write('Step (n),Time (t),Event (i),Inventory (I),Order(O),Lost Sales (L),Sales (R)\n')
for j in range(N):
    
    T = min(C)
    I = np.argmin(C)
    
    event_state = [j, T, I] + S
    out_f.write(','.join([str(v) for v in event_state]) + '\n')
    
    if I == 0: # start simulation
        C[0] = np.inf
        C[1] = 1
        S = [inv_init, 0, 0, 0]
        
        
    elif I == 1: # buy hamburgers
        
        # reset the clock for tomorrow
        C[1] = T + 1
        
        # randomly generate the demand
        D = int(np.random.normal(loc=demand_mu,scale=demand_sigma))
        S[0] -= D
        S[3] += D
        
        # compute sales losses
        if S[0] < 0:
            S[2] -= S[0] # add to the lost sales
            S[3] += S[0] # subtract from made sales
            S[0] = 0     # reset inventory to 0
        
        # do we need to place an order?
        if T % 2 >= 1 and S[0] < order_thresh:
            C[2] = T + 0.5 # schedule the order event
    
    elif I == 2: # order hanmburgers
        
        C[2] = np.inf  # don't know when next order will be placed
        C[3] = T + 1   # receive the order tomorrow
        
        S[1] = inv_max - S[0] # setup the number of patties ordered
        
    elif I == 3:
        
        C[3] = np.inf # don't know when next order will arrive
        
        S[0] += S[1]  # add inventory from order
        S[1] = 0      # reset the order amount
    
    else:
        
        print 'Weird.... how did we get here?!?!'


print S, 'Percent Loss:', S[2]*100./S[3]

out_f.close()
        
        
        
    
    
