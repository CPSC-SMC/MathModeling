# -*- coding: utf-8 -*-
"""
Recurrence Relations: Examples and Solutions

Created on Thu May 15 15:46:38 2014

@author: sbroad
"""

import numpy as np
from scipy.misc import *
import matplotlib.pyplot as plt

plt.close()

# 1. Compound Interest P(n+1) = (1+r)*P(n)
r = 0.08/12 #   r ---> interest rate
n = 24      #   n ---> time period number
P0 = 1000   #   P0 ---> initial balance
# P(n+1) = P(n) + r*P(n) ==> D P(n) = r*P(n)
#                    ==> P(n) = (1+r)**n * P(0)
P = lambda n, r, P0: P0 * (1+r)**n
print 
print 'Initial balance $%.2f' % (P0)
print 'Interest rate %f%%' % (r*100)
print 'Final balance $%.2f after %d months' % (P(n,r,P0), n) 



# 2. Paying off a loan B(n+1) = (1+r)*B(n) - Q
r = 0.05/12 #   r --> interest rate
n = 60      #   n --> time period
B0 = 12000. #   B0 ---> Initial balance
Q = 200     #   Q ---> Payment amount
# D P(n) = r*P(n) - Q
B = lambda n, r, B0, Q: B0 if n == 0 else (1+r)*B(n-1,r,B0,Q)-Q
residual = B(n,r,B0,Q)
it = 0

while abs(residual/n) >= 0.005:
    it+=1
    Q += residual / n
    residual = B(n,r,B0,Q)

print 
print 'After', it, 'iterations:'
print 'Initial balance $%.2f' % (B0)
print 'Interest rate %f%%' % (r*100)
print 'Payment amount $%.2f' % (Q)
print 'Final balance $%.2f after %d months' % (residual, n) 


# 3. Fibonacci sequence F(n+2) = F(n+1) + F(n), F(1) = 1, F(0) = 0
#    compute a generalized fibonacci sequence using y0=0, y1=1
fib1=[ 0, 1 ]
def gen_fibonacci(n, y=[ 0,1 ]):
    for i in range(len(y),n+1):
        y += [y[-1] + y[-2]]
        
    return y[-1]

print gen_fibonacci(40), gen_fibonacci(40, fib1)
print fib1

# 4. Other fibonacci sequences
fib2 = [-1,2] # different initial conditions
print gen_fibonacci(40, fib2), fib2

# 5. y(n+2) - A y(n+1) - B y(n) = 0, y(0)=y0, y(1)=y1
#    solution: y(n) = r**n
#    r**(n+2) - A r**(n+1) - B r**n = 0
#    r**2 - A r - B = 0
 

# 6. Fibonacci sequence ... direct computation
#    F(n+2) = f(n+1) + F(n); A = 1
def fibonacci(n):
    print range(1,n+1,2)
    return sum([comb(n,i,exact=1)*5**((i-1)/2) for i in range(1,n+1,2)])/2**(n-1)
    
