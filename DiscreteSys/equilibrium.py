# -*- coding: utf-8 -*-
"""
Dicrete dynamical systems, equilibrium solutions

The solution of a

Created on Sun May 18 12:56:39 2014

@author: Steven
"""

# A solution to a difference equation such that D y(n) = 0 is an equilibrium solution
# in particular, equilibrium solutions are fixed point solutions of the update function

# 1. unconstrained population growth
unconstrained = lambda y, a: (1+a) * y
# y0 = 0
print 'f(0) =', unconstrained(1, 0, 1)
# a = 0, y > 0
print 'f(10) =', unconstrained(1, 10, 0)

# 2. constrained population growth
constrained = lambda y, a, M, m = 0: y + a*(y-m)*(M-y)

# y0 = m
print 'f(0) =', constrained(0,0.00001,1000,0)

# y0 = M
print 'f(1000) =', constrained(1000,0.00001,1000,0)

# 3. logistic map
logistic = lambda y, a: a * y * (1-y)

# y = 0
