# -*- coding: utf-8 -*-
"""
Recurrence Relations: Examples and Solutions

Created on Thu May 15 15:46:38 2014

@author: sbroad
"""

import numpy as np
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

print 'Estimated Payment $', (1+r)**n * (1-r) / (1-r**n) * B0

# 3. 