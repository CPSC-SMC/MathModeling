# -*- coding: utf-8 -*-
"""
Optimization Models: Functions of one variable

Created on Thu Nov 20 08:32:55 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

"""

Newton's method on the derivative

Approximate dx = 1e-5

Approximate the 1st derivative with df(x) = (f(x+dx)-f(x))/dx

Approximate the 2nd derivative with ddf(x) = (df(x+dx)-df(x))/dx

"""

def der(f,dx=1e-6):
    return lambda x: (f(x+dx) - f(x))/dx
  
f = lambda x: (x - 2) * x * (x + 2)**2  
df = der(f)
ddf = der(df)

shift = lambda x: - df(x)/ddf(x)

x = 3
n = 0
newton_delta = shift(x)
while abs(newton_delta) > 1e-5:
    n += 1
    x += newton_delta
    newton_delta = shift(x)

print "Newton's Method"
print '  fun: {}\n  nit: {}\n    x: {}'.format(f(x),n,x)

xs = np.linspace(-2.5,1.5)
plt.plot(xs,f(xs),label='f(x)')
plt.plot(xs,df(xs),label="f'(x)")
plt.legend(loc='best')
plt.grid()

"""

minimize_scalar

"""

import scipy.optimize as opt

print 
print 'minimize_scalar'
print opt.minimize_scalar(f)