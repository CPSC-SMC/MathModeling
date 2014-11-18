# -*- coding: utf-8 -*-
"""

Nelson: Section 4.6: The Copier Problem

Created on Thu Nov 13 11:17:48 2014

@author: sbroad

"""

import numpy as np
import matplotlib.pyplot as plt

"""
Implement the stochastic process

S(n) = (Q(n),A(n),O(n))
Q(n) = number of people waiting
U(n) = number of copiers in use
O(n) = store is open

T(n) = day number, advances by 1 each day

Y(t) = state at time t

e0 = open store
e1 = customer arrives
e2 = customer finishes
e3 = close store

"""

# counters for time and iteration
j = 0
T = 0

# lists for longitudinal and state data
A = []
F = []
S = [0,0,1]

# initial clock setting
C = [0, np.inf, np.inf, 600]

# simulation parameters
mu_G = 6
mu_X = 4.6

max_copiers = 1

# setup file storage
out_f = open('copier.csv', mode = 'w')
out_f.write('Step (n),Event (i),Time (t),Queue Length(Q),In Use (U),Store Open (O),C0,C1,C2,C3\n')


# simulation loop
while max(S) > 0:
    
    j += 1
    I = np.argmin(C)
    T = min(C)
    
    if I == 0: # start simulation
        C[0] = np.inf
        C[1] = np.random.exponential(scale=mu_G)
        S = [0, 0, 1]
        
    elif I == 1: # customer arrives
        
        # reset timer for next arrival
        G = np.random.exponential(scale=mu_G)
        C[1] = T + G
        
        # if there is a machine available, set the completion time
        if S[1] < max_copiers:
            X = np.random.exponential(scale=mu_X)
            C[2] = T + X
            S[1] += 1
            
        else: # add the customer to the queue
            S[0] += 1

        # add the customer's arrival time
        A.append(T)
            
    elif I == 2: # customer finishes
        
        if S[0] == 0: # no more customers waiting
            S[1] -= 1
            C[2] = np.inf
            
        else:         # roll the completion time for the next customer
            X = np.random.exponential(scale=mu_X)
            S[0] -= 1
            C[2] = T + X
        
        # Compute the customer's wait time
        F.append(T)
    
    elif I == 3: # close store
        
        C[1] = np.inf
        C[3] = np.inf
        S[2] = 0
    
    else:
        
        print 'Weird.... how did we get here?!?!'
        
    # record state in file
    event_state = [j, I, T] + S + C
    out_f.write(','.join([str(v) for v in event_state]) + '\n')

out_f.close()

print 'Number of arrived customers  :', len(A)
print 'Number of completed customers:', len(F)
W = np.array(F) - np.array(A)

# store max wait time
if 'W_max' in globals():
    W_max.append(np.max(W))
else:
    W_max = [np.max(W)]
    
# store mean wait time
if 'W_mean' in globals():
    W_mean.append(np.mean(W))
else:
    W_mean = [np.mean(W)]

# store customers
if 'W_count' in globals():
    W_count.append(np.size(W))
else:
    W_count = [np.size(W)]
    
print 'Max wait time: ', np.max(W)
print 'Mean wait time:', np.mean(W)

plt.figure(0)
plt.hist(W)
plt.title('Histogram of customer wait time')
plt.xlabel('Customer wait time')
plt.ylabel('Frequency')
        
plt.figure(1)
plt.plot(W_count,W_max,'bo',label='Max wait time')
plt.plot(W_count,W_mean,'go',label='Mean wait time')
plt.xlabel('Number of customers')
plt.ylabel('Wait time')
plt.title('Comparing wait time to the number of customers')
plt.legend(loc='best')

