# -*- coding: utf-8 -*-
"""
Data fitting: Quadratic Regression

Created on Wed Sep 24 08:56:41 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,1,1],[1,2,4],[1,3,9],[1,4,16]])
Y = np.array([[4,2,2,1]]).T

plt.plot([1,2,3,4],[4,2,2,1],'o')

ATA = np.dot(A.T, A)
ATY = np.dot(A.T, Y)

print 'A^T*A=', ATA
print 'A^T*Y=',ATY

b = np.linalg.solve(ATA, ATY)
print 'b=', b

def f(x,b):
    return b[0] + b[1]*x+b[2]*x**2
    
x = np.linspace(0,5,21)
plt.plot(x, f(x,b))

# compute MSE
x = np.array([[1,2,3,4]])
yhat = f(x,b)
plt.plot(x,yhat,'+')
res = Y.T - yhat
print Y.T, yhat, res

print 'MSE = ', np.sum(res**2)
