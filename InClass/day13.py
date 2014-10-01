# -*- coding: utf-8 -*-
"""
Data fitting: Linear Regression

Created on Wed Sep 24 08:56:41 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1,2,3,4]])
y = np.array([[4,2,2,1]])

plt.plot(x, y, 'o')
plt.xlim(xmax = 5, xmin=0)
plt.ylim(ymax = 5, ymin = 0)

A = np.array([[1,1],[1,2],[1,3],[1,4]])
Y = y.T

ATA = np.dot(A.T, A)
ATY = np.dot(A.T, Y)

print 'A^T*A=', ATA
print 'A^T*Y=',ATY

b = np.linalg.solve(ATA, ATY)
print 'b=', b

def f(x,b):
    return b[0] + b[1]*x

yhat = f(x,b)
plt.plot(x,yhat,'+')
res = y - yhat
print y, yhat, res

print 'MSE = ', np.sum(res**2)/2