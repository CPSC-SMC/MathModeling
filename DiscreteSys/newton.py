# -*- coding: utf-8 -*-
"""
Newton's method

Created on Mon May 19 13:59:32 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def newton(f,x,dx=0.00001):
    '''
    Update function for Newton's method
    
    f ---> the function whose roots are being computed
    x ---> the current estimate for x s.t. f(x) approx 0
    dx ---> a small value to use when approximating the derivative
    '''
    df = (f(x+dx)-f(x-dx))/(2*dx)
    x += f(x)/df
    return x

# setup initial guess
plt.close(1)
func = lambda x: np.sin(2*x)
xs = np.arange(start=-np.pi,stop=np.pi,step=100)
plt.plot(xs,func(xs),'b-')
x = 1
for i in range(10):
    xnew = newton(func, x)
    plt.plot([x,xnew,xnew],[func(x),0,func(xnew)],'r-')
    x = xnew

