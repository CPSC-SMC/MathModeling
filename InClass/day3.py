# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

#1 First order homogeneous equation
# explicit rule
def f1(n, a0):
    return a0

# delta function rule    
def deltaf1(n):
    return 0
    
# update function
def updatef1(n,prev):
    return prev

# sequence with explicit rule
a = [3]
for i in range(10):
    a.append(f1(i+1, a[0]))

print a

# sequence with update function
A = [3]
for i in range(10):
    A.append(updatef1(i+1, A[-1]))

print A


#2 First order inhomogeneous equation
# explicit rule
def f2(n, a0, b):
    return a0 +b*n

# delta function rule    
def deltaf2(n, b):
    return b
    
# update function
def updatef2(n,prev,b):
    return prev + b

# sequence with explicit rule
a = [3]
for i in range(10):
    a.append(f2(i+1, a[0], 15))

print a

# sequence with update function
A = [3]
for i in range(10):
    A.append(updatef2(i+1, A[-1], 15))

print A

#Model3 from the article
# explicit rule
def f3(n, a0, b, r):
    return r**n*(a0 - b/(1-r))+b/(1-r)

# delta function rule    
# update function
def updatef3(prev,b,r):
    return r*prev + b

# sequence with explicit rule
a = [10]
for i in range(10):
    a.append(f3(i+1, a[0], -1, 1.1))

print a

# sequence with update function
A = [10]
for i in range(10):
    A.append(updatef3(A[-1], -1, 1.1))

print A

plt.plot(A,'o')