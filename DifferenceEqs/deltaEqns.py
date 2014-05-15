# -*- coding: utf-8 -*-
"""
Examples of difference equations and their solutions

Created on Thu May 15 09:31:00 2014

@author: sbroad
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close()

def diffs(y,k=1):
    ''' 
    Get the differences between adjacent terms of a sequence 
    y ---> terms of the sequence
    k ---> the order of the difference e.g. k = 1 ---> D y(n)
            k = 2 ---> D**2 y(n)
    '''
    if k >= 1:
        return diffs(np.array(y[1:]) - np.array(y[:-1]), k-1)
    elif k >= 0:
        return y 
    else:
        raise Exception('Cannot have negative order of difference')


# 1. D y(n) = 0; y(n) = y(0)
f1 = lambda n, y0 : y0 
terms = [f1(n,5) for n in range(20)]
print 'D y(n) = 0', diffs(terms)
print

# 2. D y(n) = c = y(1) - y(0); y(n) = y(0) + c*n
f2 = lambda n, y0, c: y0 + c*n
terms = [f2(n,5,-3) for n in range(20)]
print 'D y(n) = -3', diffs(terms)
print

# 3. D y(n) = g(n); y(n) = y(0) + sum(g(i),i=1 to n)
g = lambda n: n**2
f3 = lambda n, y0, func: y0 + sum([func(i+1) for i in range(n)])
terms = [f3(n, -4, g) for n in range(20)]
print 'D y(n) = g(n)', diffs(terms)
print

# 4. D y(n) = y(n); y(n) = 2**n * y(0)
f4 = lambda n, y0: 2**n * y0
terms = [f4(n, 0.225) for n in range(20)]
print 'D y(n) - y(n) = 0', diffs(terms) - np.array(terms[:-1])
print

# 5. D y(n) = c*y(n); y(n) = (1+c)**n * y(0)
f5 = lambda n, y0, c: (1+c)**n * y0
terms = [f5(n, 0.225, 0.5) for n in range(20)]
print 'D y(n) - c*y(n) = 0', diffs(terms) - 0.5*np.array(terms[:-1])
print

# 6. D**2 y(n) = 0; y(n) = y(0) + A1 n
#    A1 = y(1) - y(0)
f6 = lambda n, y0, y1: y0 + (y1 - y0)*n
y0 = 1
y1 = 2
terms = [f6(n,y0,y1) for n in range(20)]
plt.plot(terms,'+',label=r'$\Delta^2y_n=0,\,(y_0,y_1)=(%d,%d)$' % (y0,y1))
plt.legend()
print 'D**2 y(n)=0', diffs(terms,2)
print

# 7. D**3 y(n) = 0; y(n) = y(0) + A1 n + A2 n**2
#   A1 = -1.5y(0)+2y(1)-0.5y(2)
#   A2 = 0.5y(0)-y(1)+0.5y(2)
f7 = lambda n, y0, y1, y2: y0 + -0.5*(3*y0-4*y1+y2)*n + 0.5*(y0-2*y1+y2)*(n**2)
y2 = 4
terms = [f7(n,y0,y1,y2) for n in range(20)]
plt.plot(terms,'o',label=r'$\Delta^2y_n=0,\,(y_0,y_1,y_2)=(%d,%d,%d)$' % (y0,y1,y2))
plt.legend(loc='upper left')
print 'D**3 y(n)=0', diffs(terms,3)
print


# 8. D**4 y(n) = 0; y(n) = y(0) + A1 n + A2 n**2 + A3 n**3
y3 = 2
B = np.array([[1,1,1],[2,4,8],[3,9,27]])
A = np.dot(np.linalg.inv(B),np.array([y1-y0,y2-y0,y3-y0]).T)
f8 = lambda n, y0, c: y0 + np.dot(c,[n**(i+1) for i in range(len(c))])
terms = [f8(n,y0,A) for n in range(20)]
plt.plot(terms,'.',label=r'$\Delta^2y_n=0,\,(y_0,y_1,y_2,y_3)=(%d,%d,%d,%d)$' % (y0,y1,y2,y3))
plt.legend(loc='upper left')
print 'D**4 y(n)=0', diffs(terms,4)
print

