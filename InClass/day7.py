# -*- coding: utf-8 -*-
"""
Created on Mon Sep 08 09:24:16 2014

@author: sbroad
"""
import numpy as np

def fib(n):
    return 1/np.sqrt(5)*(((1+np.sqrt(5))/2)**n - ((1-np.sqrt(5))/2)**n)

print fib(0), fib(1), fib(10), fib(100)

# update function
def updatef1(prev1,prev2):
    return prev1+prev2
    
prev1 = 1
prev2 = 0
for i in range(20):
    oldprev1 = prev1
    prev1 = updatef1(prev1,prev2)
    prev2 = oldprev1
    print prev1
    
# update function
def f1(x,r,b):
    """
    r ---> 1 + growth rate
    b ---> step increase/decrease
    """
    return x*r+b


# Example: a loan
# 5% APR ---> r = 1 + 0.05/12
# initial balance = $15,000
# payment amount: b = -$240
x = 15000
for i in range(60):
    x = f1(x, 1+0.05/12, -283.10)

print 'Final balance', x


