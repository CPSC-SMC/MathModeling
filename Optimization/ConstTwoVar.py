# -*- coding: utf-8 -*-
"""
Constrained optimization

Created on Tue Dec  2 08:03:45 2014

@author: sbroad
"""

import numpy as np
import scipy.optimize as opt

# Minimize: f(x,y) = 2x + 3y
# Subject to: x^2 + y^2 <= 1
# For x, y

# objective function
f = lambda x: 2*x[0] + 3*x[1]

# constraint function: 1 - x^2 - y^2 >= 0
g = lambda x: 1 - x[0]**2 - x[1]**2

con = dict()

con['type'] = 'ineq'
con['fun'] = g

res = opt.minimize(f, (0,-1), method='SLSQP',constraints=(con))

print res
