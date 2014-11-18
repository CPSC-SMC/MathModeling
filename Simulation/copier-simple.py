# -*- coding: utf-8 -*-
"""
Copier stochastic (simple)

Created on Tue Nov 18 12:52:13 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt
from time import time
from datetime import datetime

"""

S(n) = (Q(n),A(n))
Q(n) = queue length
A(n) = copiers in use

T(n) = current time

Y(t) = S(n), where t in [T(n), T(n+1))

e0 --> open the store
e1 --> customer arrives
e2 --> customer finishes
e3 --> close store

"""

def Y(t,T,S):    
    return np.array([S[np.max(np.where(T<=s))] for s in t])
    
# setup state, clocks, and time
data = []
S = [0,0]
close_time = 360
C = [0, np.inf, np.inf, close_time]
T = 0
n = 0

# setup process parameters
mu_G = 6.0
mu_X = 4.6

# print headers
print '*************************************************'
t0 = time()
print 'Run starts:', datetime.fromtimestamp(t0).strftime('%Y-%m-%d %H:%M:%S')
print 'Step  Event    Time   Q   A      C0      C1      C2      C3'
fmt = '{:>4}{:>7}{:>8.2f}{s[0]:>4}{s[1]:>4}{c[0]:>8.2f}{c[1]:>8.2f}{c[2]:>8.2f}{c[3]:>8.2f}'
while not np.isinf(min(C)):
    
    I = int(np.argmin(C))
    T = np.min(C)

    print fmt.format(n,I,T,s=S,c=C)
    data.append([n,I,T] + S + C)
    n += 1
    
    if I == 0:
        
        C[0] = np.inf
        C[1] = np.random.exponential(scale=mu_G)
    
    elif I == 1:

        if S[1] == 0:
            S[1] = 1
            C[2] = T + np.random.exponential(scale=mu_X)
        else:
            S[0] += 1
            
        C[1] = T + np.random.exponential(scale=mu_G)

    elif I == 2:
        if S[0] == 0:
            S[1] = 0
            C[2] = np.inf
            
        else:
            S[0] -= 1
            C[2] = T + np.random.exponential(scale=mu_X)
        
    elif I == 3:
        
        C[1] = np.inf
        C[3] = np.inf
        
    else:
        
        S = []
        C = [np.inf]
        
print fmt.format(n,I,T,s=S,c=C)
print 'Run time:', time()-t0, 's'
print

data.append([n,I,T] + S + C)
data = np.array(data)

ts = np.linspace(0,T,1001)
ys = Y(ts,data[:,2],data[:,4])
print 'Idle Time: {:6.2f} minutes'.format( T - np.sum(ys)*T/np.size(ys))
print 'Over Time: {:6.2f} minutes'.format(T - close_time)

