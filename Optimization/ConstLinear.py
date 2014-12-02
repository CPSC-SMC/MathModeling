# -*- coding: utf-8 -*-
"""
Constrained Linear Optimization

Created on Tue Dec  2 08:44:42 2014

@author: sbroad
"""

import numpy as np
import scipy.optimize as opt

'''
Minimize: f(x) = 2*x1 - 3*x2 - x3 + 4*x4
Subject to:
    x1 + x2 + x3 + x4 <= 20
    x1 >= x2
    x4 >= x3/5 + 3*x2/10
    
Where:
    x in [0,inf)**4
'''

# Objective function
f = lambda x: np.dot(x,[2,-3,-1,4])

# Constraints
cons = (dict(),dict(),dict())

# Constraint 1: 20 - x1 - x2 - x3 - x4 >= 0
g0 = lambda x: 20 - np.dot(x,[1,1,1,1])
cons[0]['type'] = 'ineq'
cons[0]['fun'] = g0

# Constraint 2: x1 - x2 >= 0
g1 = lambda x: np.dot(x,[1,-1,0,0])
cons[1]['type'] = 'ineq'
cons[1]['fun'] = g1

# Constraint 3: -0.2 x2 - 0.3 x3 + x4 >= 0
g2 = lambda x: np.dot(x,[0,-0.2,-0.3,1])
cons[2]['type'] = 'ineq'
cons[2]['fun'] = g2

# Bounds
bnds = ((0,np.inf),(0,np.inf),(0,np.inf),(0,np.inf))
res = opt.minimize(f,(0,0,0,0), method='SLSQP', bounds=bnds, constraints=cons)

print res
